from django.urls import path
from .views import (RealtorDetailApiView,AddAdsApiView,AllAdsApiView,
                    UpdateAdsApiView,DeleteAdsApiView,CloseAdsApiView,
                    AdsDetailApiView,AllMyAdsApiView,AllRealtorApiView,
                    SearchApiView)

app_name='ads'
urlpatterns =[
    path('realtors/',AllRealtorApiView.as_view(),name='all-realtors'),
    path('realtor/<int:id>/',RealtorDetailApiView.as_view(),name='detail-realtor'),
    path('update/<int:id>/',UpdateAdsApiView.as_view(),name='update-ads'),
    path('delete/<int:id>/',DeleteAdsApiView.as_view(),name='delete-ads'),
    path('close/<int:id>/',CloseAdsApiView.as_view(),name='close-ads'),
    path('add/',AddAdsApiView.as_view(),name='add-ads'),
    path('my-ads/',AllMyAdsApiView.as_view(),name='my-ads'),
    path('detail/<int:id>/',AdsDetailApiView.as_view(),name='detail-ads'),
    path('search/<str:data>/',SearchApiView.as_view(),name='search'),
    path('',AllAdsApiView.as_view(),name='all=ads'),

]