from django.urls import path
from . import views

app_name = 'hikaku'

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('mypage/', views.MyPage.as_view(), name='mypage'),
    path('search/', views.Search.as_view(), name='search'),
    path('search_result/', views.SearchResult.as_view(), name='search_result'),
    path('offer_list/', views.OfferList.as_view(), name='offer_list'),
]