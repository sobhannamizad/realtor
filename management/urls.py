from django.urls import path
from .views import(AllRealtorApiView,AllUnacceptedRealtorApiView,AllBlockRealtorApiView,
                   RejectRequestApiView,BlockRealtorApiView,ActiveRealtorApiView,
                   AllUnacceptedAdsApiView,ActiveAdsApiView,DeleteAdsApiView,
                   AddBalanceToUserApiView)

app_name='management'

urlpatterns=[
    path('',AllRealtorApiView.as_view(),name='all-realtor'),
    path('unaccepted/',AllUnacceptedRealtorApiView.as_view(),name='all-unaccepted-realtor'),
    path('all-blocked/',AllBlockRealtorApiView.as_view(),name='all-blocked'),
    path('reject/<int:id>/',RejectRequestApiView.as_view(),name='reject'),
    path('block/<int:id>/',BlockRealtorApiView.as_view(),name='block'),
    path('active/<int:id>/',ActiveRealtorApiView.as_view(),name='active'),
    path('active/ads/<int:id>/',ActiveAdsApiView.as_view(),name='active-ads'),
    path('delete/ads/<int:id>/',DeleteAdsApiView.as_view(),name='delete-ads'),
    path('all/ads/',AllUnacceptedAdsApiView.as_view(),name='all-unaccepted-ads'),
    path('add-balance/',AddBalanceToUserApiView.as_view(),name='add-balance'),
]