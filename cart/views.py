from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart
from book.models import Book
from django.contrib import messages

@login_required
def add_to_cart(request, book_id):
    # Get the book object based on book_id
    book = get_object_or_404(Book, id=book_id)

    # If the user already has this book in their cart, just increment the quantity
    cart_item, created = Cart.objects.get_or_create(user=request.user, book=book)

    if not created:
        # If the item already exists, increment the quantity
        cart_item.quantity += 1
    cart_item.save()

    messages.success(request, f"{book.title} has been added to your cart!")
    return redirect("cart_view")

# cart/views.py
@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.book.price * item.quantity for item in cart_items)  # Assuming Book model has a `price` field

    return render(request, "cart/cart.html", {"cart_items": cart_items, "total_price": total_price})

