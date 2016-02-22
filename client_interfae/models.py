from django.db import models
from django.utils import timezone


# Create your models here.

class Sender(models.Model):
    id = models.CharField(max_length=250, primary_key=True)
    jid = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)


class Media(models.Model):
    type = models.CharField(max_length=250)
    url = models.CharField(max_length=500)
    local_path = models.CharField(max_length=250)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.type


class Fling(models.Model):
    id = models.CharField(max_length=250, primary_key=True)
    created_at = models.DateTimeField('created at')
    country = models.CharField(max_length=250)
    media = models.ForeignKey(Media)
    sender = models.ForeignKey(Sender)

    def __str__(self):
        return "{0} - {1}".format(self.id, self.country)
