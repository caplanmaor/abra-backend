from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    title = models.TextField()
    body = models.TextField()
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='reciever', on_delete=models.CASCADE)
    is_read = models.BooleanField(default = False)

