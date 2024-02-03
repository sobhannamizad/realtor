from django.urls import path
from .views import (UserRegisterApiView,BecomeRealtorApiView,
                    UpdateUserApiView,UpdateRealtorApiView
                    )
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns =[
    path('register/',UserRegisterApiView.as_view()),
    path('BecomeRealtor/',BecomeRealtorApiView.as_view()),
    path('update/',UpdateUserApiView.as_view()),
    path('update/realtor/',UpdateRealtorApiView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]