from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    phone = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.address

