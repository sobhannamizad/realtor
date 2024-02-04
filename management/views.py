from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from accounts.models import Realtor
from accounts.serializers import RealtorSerializer
from ads.models import Property
from ads.serializers import PropertySerializer

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
            realtor.delete()
        # TODO : send sms to user and say request is reject
            return Response({'detail':'request reject successfully'},status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'invalid id'}, status=status.HTTP_400_BAD_REQUEST)


class BlockRealtorApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,id):
        try:
            realtor = Realtor.objects.filter(id=id)
            realtor.is_block =True
            realtor.save()
            # TODO : send sms to user and say request is reject
            return Response({'detail':'realtor block successfully'},status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'invalid id'}, status=status.HTTP_400_BAD_REQUEST)

class ActiveRealtorApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,id):
        try:
            realtor = Realtor.objects.filter(id=id)
            realtor.is_active = True
            realtor.save()
            # TODO : send sms to user and say request is reject
            return Response({'detail': 'realtor active successfully'}, status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'invalid id'}, status=status.HTTP_400_BAD_REQUEST)

class ActiveAdsApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,id):
        try:
            ad = Property.objects.filter(id=id)
            ad.is_active = True
            ad.save()
            # TODO : send sms to user and say request is reject
            return Response({'detail': 'ad active successfully'}, status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'invalid id'}, status=status.HTTP_400_BAD_REQUEST)

class DeleteAdsApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,id):
        ad = Property.objects.filter(id=id)
        if not ad.exists():
            return Response({'detail':'invalid id'},status=status.HTTP_400_BAD_REQUEST)
        ad[0].delete()
        # TODO : send sms to user and say ads is deleted
        return Response({'detail':'ads delete successfully'},status=status.HTTP_200_OK)

class AllUnacceptedAdsApiView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request):
        ads= Property.objects.filter(is_active=False)
        ser_data = PropertySerializer(instance=ads, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)
