from django.urls import path
from . import views

urlpatterns = [

    path('verification', views.ListVerification_method.as_view(), name='verification'),
    path('verification/<int:pk>/', views.DetailVerification_method.as_view(), name='singleverification'),
    path('account-type', views.ListAccount_type.as_view(), name='account'),
    path('account-type/<int:pk>/', views.DetailAccount_type.as_view(), name='singleaccount'),
    path('gender', views.ListGender.as_view(), name='gender'),
    path('gender/<int:pk>/', views.DetailGender.as_view(), name='singlegender'),
    path('profile', views.ListProfile.as_view(), name='profile'),
    path('profile/<int:pk>/', views.DetailProfile.as_view(), name='singleprofile')

]
