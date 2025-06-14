from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    class Meta:
        app_label = 'customer'
    def __str__(self):
        return self.name
    