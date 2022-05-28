from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return('200 - user created')

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return('200 - user logged in')

#csrf_exempt
def send_message(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            print('logged in')
        else:       
            # Do something for anonymous users.
             print('plesae log in')