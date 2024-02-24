from django.urls import path
from carts.views import (MyCartsApiView)

app_name = 'carts'

urlpatterns = [
    path('',MyCartsApiView.as_view(),name='my-cart'),
]