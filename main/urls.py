from django.urls import path
from . import views

urlpatterns = [
    path('trial', views.trial, name='trial'),
    path('biography', views.biography, name='biography'),
    path('contacts', views.contacts, name='contacts'),
    path('login', views.login, name='login'),
]