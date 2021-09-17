from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
]