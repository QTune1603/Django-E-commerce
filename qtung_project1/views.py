from django.shortcuts import render
from services.book_service.book.models import Book  # Assuming you have a Book model
from django.db.models import Q


def home_view(request, category=None):
    query = request.GET.get('q', '')
    books = Book.objects.all()

    if query:
        books = books.filter(Q(title__icontains=query) | Q(description__icontains=query))

    if category:
        if category == "bestsellers":
            books = books.filter(is_bestseller=True)
        elif category == "new":
            books = books.filter(is_new=True)
        elif category == "sale":
            books = books.filter(is_sale=True)
        elif category == "featured":
            books = books.filter(is_featured=True)

    return render(request, 'home.html', {
        'books': books,
        'query': query,
        'active_category': category or 'all',
    })