from django.urls import path
from .views import (UserRegisterApiView,BecomeRealtorApiView,
                    UpdateUserApiView,UpdateRealtorApiView,
                    VoteRealtorApiView
                    )
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

app_name ='accounts'

urlpatterns =[
    path('register/',UserRegisterApiView.as_view(),name='register'),
    path('BecomeRealtor/',BecomeRealtorApiView.as_view(),name='BecomeRealtor'),
    path('update/',UpdateUserApiView.as_view(),name='update-user'),
    path('vote/',VoteRealtorApiView.as_view(),name='vote'),
    path('update/realtor/',UpdateRealtorApiView.as_view(),name='update-realtor'),
    path('token/', TokenObtainPairView.as_view(),name='token'),
    path('token/refresh/', TokenRefreshView.as_view(),name='refresh-token'),
]