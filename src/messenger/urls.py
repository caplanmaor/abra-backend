from django.urls import path
from . import views

urlpatterns = [
    path('create_user', views.create_user, name='create_user'),
    path('login_user', views.login_user, name='login_user'),
    path('send_message', views.send_message, name='send_message'),
    path('read_message', views.read_message, name='read_message'),
    path('read_all_messages', views.read_all_messages, name='read_all_messages'),
    path('read_unread_messages', views.read_unread_messages, name='read_unread_messages'),
    path('delete_message', views.delete_message, name='delete_message'),
]