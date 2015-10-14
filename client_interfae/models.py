from django.db import models
from django.utils import timezone

# Create your models here.

class Sender(models.Model):
    sender_id = models.CharField(max_length=250)
    jid  = models.CharField(max_length=250)
    def __str__(self):
        return self.sender_id

class Media(models.Model):
    type = models.CharField(max_length=250)
    url = models.CharField(max_length=500)
    local_path = models.CharField(max_length=250)
    def __str__(self):
        return self.type

class Fling(models.Model):
    fling_id = models.CharField(max_length=250)
    created_at = models.DateTimeField('created at')
    country  = models.CharField(max_length=250)
    media = models.ForeignKey(Media)
    sender = models.ForeignKey(Sender)