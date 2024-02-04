from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from .serializers import UserSerializer,RealtorSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Realtor
from A.utils import UserNotAuthenticated

class UserRegisterApiView(APIView):
    permission_classes = (UserNotAuthenticated,)
    def post(self,request):
        """
        get full_name phone_number code (optional) and password then create user
        """
        ser_data =UserSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

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