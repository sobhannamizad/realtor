from django.urls import path
from .views import(AllRealtorApiView,AllUnacceptedRealtorApiView,AllBlockRealtorApiView,
                   RejectRequestApiView,BlockRealtorApiView,ActiveRealtorApiView,
                   AllUnacceptedAdsApiView,ActiveAdsApiView,DeleteAdsApiView)

urlpatterns=[
    path('',AllRealtorApiView.as_view()),
    path('unaccepted/',AllUnacceptedRealtorApiView.as_view()),
    path('all-blocked/',AllBlockRealtorApiView.as_view()),
    path('reject/<int:id>/',RejectRequestApiView.as_view()),
    path('block/<int:id>/',BlockRealtorApiView.as_view()),
    path('active/<int:id>/',ActiveRealtorApiView.as_view()),
    path('active/ads/<int:id>/',ActiveAdsApiView.as_view()),
    path('delete/ads/<int:id>/',DeleteAdsApiView.as_view()),
    path('all/ads/',AllUnacceptedAdsApiView.as_view()),
]