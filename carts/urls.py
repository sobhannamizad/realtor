from django.urls import path
from carts.views import (MyCartsApiView,AddToMyCartApiVew,PayApiView)

app_name = 'carts'

urlpatterns = [
    path('',MyCartsApiView.as_view(),name='my-cart'),
    path('add/<int:property_id>/',AddToMyCartApiVew.as_view(),name='add-to-cart'),
    path('pay/<int:cart_id>/',PayApiView.as_view(),name='pay'),
]