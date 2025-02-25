from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name