import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')

    def __str__(self):
        return self.name


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')

    def __str__(self):
        return self.body

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)
