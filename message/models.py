import django.utils.timezone
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
         return self.user.first_name + ' ' + self.user.last_name


class Messages(models.Model):
    message = models.CharField(max_length=500, null=False, blank=False)
    create_at = models.DateTimeField(default=datetime.now(), blank=False)
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
    reciver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reciver')

    def __str__(self):
        return self.message

