import datetime

from django.db import models
from django.utils import timezone

from django.core.validators import MinLengthValidator, MaxLengthValidator

# class User(models.Model):
#     name = models.CharField(max_length=200)
#     created_at = models.DateTimeField('date created')

#     def __str__(self):
#         return self.name

class Tweet(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, validators=[
        MinLengthValidator(3),
        MaxLengthValidator(20)
    ])
    message = models.CharField(max_length=50, validators=[
        MinLengthValidator(4),
        MaxLengthValidator(50)
    ])
    pub_date = models.DateTimeField('publication date')

    class Meta:
        ordering = ['-pub_date', 'username']

    def __str__(self):
        return self.message
