from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from accounts.models import Realtor,User
from accounts.serializers import RealtorSerializer
from ads.models import Property
from ads.serializers import PropertySerializer
from management.serializers import BalanceSerializer
from accounts.tasks import send_email

class AllRealtorApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request):
        all_realtor = Realtor.objects.filter(is_active =True,is_block =False)
        ser_data = RealtorSerializer(instance=all_realtor,many=True)
        return Response(ser_data.data,status=status.HTTP_200_OK)


class AllUnacceptedRealtorApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request):
        all_realtor = Realtor.objects.filter(is_active=False, is_block=False)
        ser_data = RealtorSerializer(instance=all_realtor, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)

class AllBlockRealtorApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request):
        all_realtor = Realtor.objects.filter(is_block=True)
        ser_data = RealtorSerializer(instance=all_realtor, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)

class RejectRequestApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,id):
        try:
            realtor = Realtor.objects.get(id=id)
            user = realtor.user
            realtor.delete()
            message = f"your request for be come a realtor in our website rejected\n realtor"
            send = send_email.apply_async([user.email, message])
            return Response({'detail':'request reject successfully'},status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'invalid id'}, status=status.HTTP_400_BAD_REQUEST)


class BlockRealtorApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,id):
        try:
            realtor = Realtor.objects.get(id=id)
            realtor.is_block =True
            realtor.save()
            message = f"your account in our website blocked \n realtor"
            subject = "account block"
            send = send_email.apply_async([realtor.user.email, message,subject])
            return Response({'detail':'realtor block successfully'},status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'invalid id'}, status=status.HTTP_400_BAD_REQUEST)

class ActiveRealtorApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,id):
        try:
            realtor = Realtor.objects.get(id=id)
            realtor.is_active = True
            realtor.save()
            message = f"your request for be come a realtor in our website accepted successfully \n realtor"
            subject = "account activate"
            send = send_email.apply_async([realtor.user.email, message,subject])
            return Response({'detail': 'realtor active successfully'}, status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'invalid id'}, status=status.HTTP_400_BAD_REQUEST)

class ActiveAdsApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,id):
        try:
            advertisement = Property.objects.get(id=id)
            advertisement.is_active = True
            advertisement.save()
            message = f"your advertisement {advertisement.title} - successfully active \n realtor"
            subject = "ads activate"
            send = send_email.apply_async([advertisement.owner.email, message,subject])
            return Response({'detail': 'ad active successfully'}, status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'invalid id'}, status=status.HTTP_400_BAD_REQUEST)

class DeleteAdsApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,id):
        try:
            advertisement = Property.objects.get(id=id)
            advertisement.delete()
            message = f"your advertisement {advertisement.title} - rejected \n realtor"
            subject = "reject Ads"
            send = send_email.apply_async([advertisement.owner.email, message,subject])
            return Response({'detail':'advertisement delete successfully'},status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'invalid id'}, status=status.HTTP_400_BAD_REQUEST)

class AllUnacceptedAdsApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request):
        advertisements= Property.objects.filter(is_active=False)
        ser_data = PropertySerializer(instance=advertisements, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class AddBalanceToUserApiView(APIView):
    permission_classes = (IsAdminUser,)
    def post(self,request):
        # get id(user id) and amount
        ser_data = BalanceSerializer(data=request.POST)
        if ser_data.is_valid():
            cd = ser_data.validated_data
            try:
                user = User.objects.get(id=cd['id'])
            except:
                return Response({"detail":'invalid id'})
            user.balance += cd['amount']
            user.save()
            return Response({"detail":f'to {user.full_name} - add {cd["amount"]} - successfully'},status=status.HTTP_200_OK)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)











