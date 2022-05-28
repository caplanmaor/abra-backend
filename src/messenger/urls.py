from django.urls import path
from . import views

urlpatterns = [
    path('create_user', views.create_user, name='create_user'),
    path('login_user', views.login_user, name='login_user'),
    path('send_message', views.send_message, name='send_message')
]