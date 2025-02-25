from django.shortcuts import render
from book.models import Book  # Assuming you have a Book model

def home_view(request):
    books = Book.objects.all()
    return render(request, "home.html", {"books": books})
    