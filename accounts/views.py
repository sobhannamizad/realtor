from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer,RealtorSerializer,VoteSerializer,OTPSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Realtor,Vote,OTP,User
from A.utils import UserNotAuthenticated
from A.utils import create_verify_code
from accounts.tasks import send_email
import pytz
from datetime import timedelta,datetime

class UserRegisterApiView(APIView):
    permission_classes = (UserNotAuthenticated,)
    def post(self,request):
        """
        get full_name email code (optional) and password then create user
        """
        ser_data = UserSerializer(data=request.POST)
        if ser_data.is_valid():
            code = create_verify_code()
            user = ser_data.save()
            OTP.objects.create(user=user, code=code)
            request.session['user_email'] = user.email
            send = send_email.apply_async([user.email, code])
            return Response(
                   {'detail': 'user register successfully please check your email and verify your account'},
                status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class BecomeRealtorApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        """
        get address / rate / description
        """
        if request.user.is_realtor ==True:
            return Response({"details":"you are a realtor"},status=status.HTTP_400_BAD_REQUEST)
        ser_data =RealtorSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save(user=request.user)
            request.user.is_realtor =True
            request.user.save()
            context ={'response':'your request received successfully','details':ser_data.data}
            return Response(context,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class VerifyAccountApiView(APIView):
    def post(self,request):
        ser_data = OTPSerializer(data=request.POST)
        if ser_data.is_valid():
            try:
                user_email = request.session.get('user_email')
                user = User.objects.get(email=user_email)
                otp = OTP.objects.get(user=user)
            except:
                return Response({"detail":'error'},status=status.HTTP_400_BAD_REQUEST)
            now = datetime.now().replace(tzinfo=pytz.UTC)
            expire = otp.created_at + timedelta(minutes=5)
            if expire > now and otp.code == ser_data.validated_data['code'] and otp.user == user:
                user.is_active = True
                user.save()
                del user_email
                request.session.save()
                otp.delete()
                return Response({'detail':'your account verify successfully'},status=status.HTTP_200_OK)
            return Response({"detail": 'error'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateUserApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        ser_data = UserSerializer(instance=request.user,data=request.POST,partial=True)
        if ser_data.is_valid():
            if ser_data.validated_data['password']:
                return Response({'detail':'you can not change your password in here'},status=status.HTTP_403_FORBIDDEN)
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_200_OK)
        return Response(ser_data.errors,status=status.HTTP_401_UNAUTHORIZED)

class UpdateRealtorApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        try:
            realtor =Realtor.objects.get(user=request.user)
            ser_data = RealtorSerializer(instance=realtor,data=request.POST,partial=True)
            if ser_data.is_valid():
                ser_data.save()
                return Response(ser_data.data,status=status.HTTP_200_OK)
            return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'detail':'error (you ate not realtor)'},status=status.HTTP_400_BAD_REQUEST)


class VoteRealtorApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        ser_data =VoteSerializer(data=request.POST)
        if ser_data.is_valid():
            cd = ser_data.validated_data
            try:
                realtor = Realtor.objects.get(id=cd['realtor'])
            except:
                return Response({'detail':'invalid id'},status=status.HTTP_400_BAD_REQUEST)
            try:
                vote = Vote.objects.get(user=request.user,realtor=realtor)
                vote.vote = cd['vote']
                vote.save()
            except:
                Vote.objects.create(user=request.user,realtor=realtor,vote=cd['vote'])
            average = realtor.calculate_average_stars()
            realtor.stars_average = average
            realtor.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
