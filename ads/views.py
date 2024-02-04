from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Realtor
from accounts.serializers import RealtorSerializer
from .serializers import PropertySerializer
from .models import Property
from rest_framework.permissions import IsAuthenticated


class RealtorDetailApiView(APIView):
    def get(self,request,id):
        try:
            realtor = Realtor.objects.get(id=id)
            ser_data = RealtorSerializer(instance=realtor)
            return Response(ser_data.data,status=status.HTTP_200_OK)
        except:
            return Response({'detail':'invalid id'},status=status.HTTP_400_BAD_REQUEST)

class AllRealtorApiView(APIView):
    def get(self,request):
        realtors = Realtor.objects.filter(is_active=True,is_block=False)
        ser_data = RealtorSerializer(instance=realtors,many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)

class AllAdsApiView(APIView):
    def get(self,request):
        ads = Property.objects.filter(is_active=True,is_close=False)
        ser_data = PropertySerializer(instance=ads,many=True)
        return Response(ser_data.data,status=status.HTTP_200_OK)

class AddAdsApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        """
        get: address /title/ price /description/ type /and optional data -> prepayment /image/
        """
        try:
            ser_data =PropertySerializer(data=request.POST)
            if ser_data.is_valid():
                ser_data.save(owner=request.user.realtor)
                return Response(ser_data.data,status=status.HTTP_200_OK)
            return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'detail': 'you are not a realtor'}, status=status.HTTP_401_UNAUTHORIZED)

class UpdateAdsApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,id):
        try:
            ad =Property.objects.filter(id=id)
            ser_data = PropertySerializer(instance=ad,data=request.POST,partial=True)
            if ser_data.is_valid():
                ser_data.save()
                return Response(ser_data.data,status=status.HTTP_200_OK)
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'detail': 'invalid id'}, status=status.HTTP_400_BAD_REQUEST)


class DeleteAdsApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self,request,id):
        ad = Property.objects.filter(id=id)
        if not ad.exists():
            return Response({'detail': 'invalid id'},status=status.HTTP_400_BAD_REQUEST)
        if ad[0].owner == request.user.realtor:
            ad[0].delete()
            return Response({'detail':'ad deleted successfully'},status=status.HTTP_200_OK)
        return Response({'detail':'you are not the owner'},status=status.HTTP_400_BAD_REQUEST)


class CloseAdsApiView(APIView):
    def get(self,request,id):
        ad = Property.objects.filter(id=id)
        if not ad.exists():
            return Response({'detail': 'invalid id'},status=status.HTTP_400_BAD_REQUEST)
        ad = ad.first()
        if ad.owner == request.user.realtor:
            ad.is_close = True
            ad.save()
            return Response({'detail': 'ad close successfully'}, status=status.HTTP_200_OK)
        return Response({'detail': 'you are not the owner'}, status=status.HTTP_400_BAD_REQUEST)

class AdsDetailApiView(APIView):
    def get(self,request,id):
        ad = Property.objects.filter(id=id)
        if not ad.exists():
            return Response({'detail': 'invalid id'},status=status.HTTP_400_BAD_REQUEST)
        ser_data = PropertySerializer(instance=ad[0])
        context ={'ads':ser_data.data,'more detail':[ad[0].owner.description,ad[0].owner.rate,ad[0].owner.address]}
        return Response(context,status=status.HTTP_200_OK)

class AllMyAdsApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        if not request.user.realtor:
            return Response({"detail":'you are not a realtor'},status=status.HTTP_400_BAD_REQUEST)
        ads = Property.objects.filter(owner=request.user.realtor)
        ser_data = PropertySerializer(instance=ads,many=True)
        return Response(ser_data.data,status=status.HTTP_200_OK)