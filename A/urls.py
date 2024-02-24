from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('management/',include('management.urls',namespace='management')),
    path('carts/',include('carts.urls',namespace='carts')),
    path('',include('ads.urls',namespace='ads')),
]
