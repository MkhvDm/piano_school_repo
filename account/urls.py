from django.urls import path
from . import views
from account.views import LoginView

app_name = 'account'

urlpatterns = [
    path('', views.account, name='account'),
    path('sign_up/', views.sign_up, name='sign_up'),
    # path('login/', views.login_v, name='login'),
    path('login/', LoginView.as_view(template_name="account/login.html")),#, name='login'),
    path('logout/', views.logout_v, name='logout'),
    path('settings/', views.settings, name='settings'),

]