from django.urls import path
from .views import (RealtorDetailApiView,AddAdsApiView,AllAdsApiView,
                    UpdateAdsApiView,DeleteAdsApiView,CloseAdsApiView,
                    AdsDetailApiView,AllMyAdsApiView,AllRealtorApiView)

urlpatterns =[
    path('realtor/',AllRealtorApiView.as_view()),
    path('realtor/<int:id>/',RealtorDetailApiView.as_view()),
    path('update/<int:id>/',UpdateAdsApiView.as_view()),
    path('delete/<int:id>/',DeleteAdsApiView.as_view()),
    path('close/<int:id>/',CloseAdsApiView.as_view()),
    path('add/',AddAdsApiView.as_view()),
    path('my-ads/',AllMyAdsApiView.as_view()),
    path('',AllAdsApiView.as_view()),
    path('detail/<int:id>/',AdsDetailApiView.as_view()),
]