from carts.models import Cart
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

