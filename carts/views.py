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

class PayApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,cart_id):
        try:
            cart = Cart.objects.get(id=cart_id)
            if cart.property.type == 'S' and cart.user == request.user and cart.property.is_close == False and request.user.balance >= cart.property.price:
                request.user.balance = request.user.balance - cart.property.price
                request.user.save()
                cart.is_paid = True
                cart.save()
                property = cart.property
                property.is_close = True
                property.is_active = False
                property.save()
                return Response({"detail":'cart paid successfully'},status=status.HTTP_201_CREATED)

            if cart.user == request.user and cart.property.is_close == False and request.user.balance >= cart.property.prepayment:
                request.user.balance = request.user.balance - cart.property.prepayment
                request.user.save()
                cart.is_paid = True
                cart.save()
                property = cart.property
                property.is_close = True
                property.is_active = False
                property.save()
                return Response({"detail":'cart paid  a prepayment successfully'},status=status.HTTP_201_CREATED)
            
            return Response('error',status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'detail':'invalid id'},status=status.HTTP_400_BAD_REQUEST)
