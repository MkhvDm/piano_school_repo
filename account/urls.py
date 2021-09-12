from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('login/', views.account, name='account'),
    path('registration/', views.registration, name='registration'),
]