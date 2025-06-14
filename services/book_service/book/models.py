from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default="This is a placeholder description.")
    stock = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    is_bestseller = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    class Meta:
        app_label = 'book'