from django.urls import path
from . import views


app_name = 'timepad'

urlpatterns = [
    path('', views.timepad_default, name='timepad_default'),
    path('<int:year>/<int:month>/', views.timepad, name='timepad'),
    path('events/<int:year>/<int:month>', views.all_events, name='all_events'),
    path('events/<int:year>/<int:month>/<int:day>/', views.date_events, name='date_events'),
    # path('', views.account, name='account'),
    # path('sign_up/', views.sign_up, name='sign_up'),
    # path('login/', LoginView.as_view(template_name="account/login.html")),#, name='login'),

]