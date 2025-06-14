from django.db import models
from services.customer_service.customer.models import Customer
from services.book_service.book.models import Book

# Create your models here.
class CommentRecommendation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f"Comment by {self.customer.name} on {self.book.title}"
