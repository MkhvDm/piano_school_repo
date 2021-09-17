from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.account, name='account'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_v, name='login'),
    path('logout/', views.logout_v, name='logout'),

]