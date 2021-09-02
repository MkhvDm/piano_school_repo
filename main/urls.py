from django.urls import path
from . import views

urlpatterns = [
    path('welcome', views.welcome_page, name='welcome_page'),
    path('biography', views.biography, name='biography'),
    path('contacts', views.contacts, name='contacts'),
]