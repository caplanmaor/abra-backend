from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q
from messenger.models import Message
from django.core import serializers

def create_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse(status=200)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return HttpResponse(status=200)

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

def read_message(request):
    if request.method == "GET":
        message = Message.objects.filter(receiver_id=request.user.id).first()
        # set message as read
        message.is_read = True
        message.save()
        message_json = serializers.serialize("json", [message])
        return HttpResponse(message_json)

def read_all_messages(request):
    if request.method == "GET":
        messages = Message.objects.filter(receiver_id=request.user.id).all()
        # set messages as read
        for message in messages:
            message.is_read = True
            message.save()
        messages_json = serializers.serialize("json", messages)
        return HttpResponse(messages_json)

def read_unread_messages(request):
    if request.method == "GET":
        messages = Message.objects.filter(receiver_id=request.user.id).filter(is_read=False).all()
        # set messages as read
        for message in messages:
            message.is_read = True
            message.save()
        messages_json = serializers.serialize("json", messages)
        return HttpResponse(messages_json)

def delete_message(request):
    if request.method == "POST":
        id = request.POST['message_id']
        message = Message.objects.filter(Q(receiver_id=request.user.id) | Q(owner_id=request.user.id)).filter(id=id).first()
        message.delete()
        return HttpResponse(status=200)