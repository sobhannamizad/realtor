from carts.models import Cart
from ads.models import Property
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from carts.serializers import CartSerializer

class MyCartsApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        carts = request.user.cart.all()
        result = CartSerializer(instance=carts,many=True)
        return Response(result.data,status=status.HTTP_200_OK)

class AddToMyCartApiVew(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,property_id):
        try:
            property = Property.objects.get(id=property_id)
        except:
            return Response({'detail':'invalid id'},status=status.HTTP_400_BAD_REQUEST)
        cart = Cart.objects.create(user=request.user,property=property)
        result = CartSerializer(instance=cart)
        return Response(result.data,status=status.HTTP_201_CREATED)


