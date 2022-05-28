from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from messenger.models import Message

# import json
@csrf_exempt
def create_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse(status=200)

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return HttpResponse(status=200)

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            current_user = request.user
            title = request.POST['title']
            body = request.POST['body']
            receiver = request.POST['receiver']
            rec_user = User.objects.get(username=receiver)
            message = Message.objects.create(title=title, body=body, owner_id=current_user.id, receiver_id=rec_user.id)
            message.save()
            return HttpResponse(status=200)
        else:       
            # Do something for anonymous users.
            return HttpResponse(status=500)