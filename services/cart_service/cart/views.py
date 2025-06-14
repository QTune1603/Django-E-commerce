from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render, redirect
from .models import Cart, CartItem
from services.book_service.book.models import Book
from services.customer_service.customer.models import Customer
from django.contrib.auth import get_user_model

User = get_user_model()

@require_POST
def add_to_cart(request, book_id):
    user = User.objects.using('default').get(pk=request.user.pk)
    customer = Customer.objects.using('default').get(user=user)

    # Kiểm tra book_id tồn tại trong DB default
    book_exists = Book.objects.using('default').filter(id=book_id).exists()
    if not book_exists:
        return render(request, 'cart/error.html', {'message': 'Book not found.'})

    cart = Cart.objects.using('cart').filter(customer=customer.id).first()
    if not cart:
        cart = Cart.objects.using('cart').create(customer=customer.id)

    # Dùng book_id trực tiếp thay vì book instance
    item = CartItem.objects.using('cart').filter(cart_id=cart.id, book_id=book_id).first()
    if not item:
        item = CartItem.objects.using('cart').create(cart_id=cart.id, book_id=book_id, quantity=1)
    else:
        item.quantity += 1
        item.save(using='cart')

    return redirect('cart_view')


@require_POST
def remove_from_cart(request, item_id):
    user = User.objects.using('default').get(pk=request.user.pk)
    customer = Customer.objects.using('default').get(user=user)

    cart = Cart.objects.using('cart').filter(customer=customer.id).first()
    if cart:
        item = get_object_or_404(CartItem.objects.using('cart'), id=item_id, cart_id=cart.id)
        item.delete(using='cart')

    return redirect('cart_view')

def cart_view(request):
    user = User.objects.using('default').get(pk=request.user.pk)
    customer = Customer.objects.using('default').get(user=user)

    cart = Cart.objects.using('cart').filter(customer=customer.id).first()
    if not cart:
        cart = Cart.objects.using('cart').create(customer=customer.id)

    cart_items = CartItem.objects.using('cart').filter(cart_id=cart.id)

    # Lấy danh sách book tương ứng từ DB default
    book_ids = [item.book_id for item in cart_items]
    books = {book.id: book for book in Book.objects.using('default').filter(id__in=book_ids)}

    # Gắn thêm giá từ book đúng
    for item in cart_items:
        item.book_price = books[item.book_id].price

    total = sum(item.book_price * item.quantity for item in cart_items)

    return render(request, 'cart/cart_view.html', {
        'cart_items': cart_items,
        'total': total
    })


@require_POST
def update_quantity(request, item_id):
    user = User.objects.using('default').get(pk=request.user.pk)
    customer = Customer.objects.using('default').get(user=user)

    cart = Cart.objects.using('cart').filter(customer=customer.id).first()
    if not cart:
        return redirect('cart_view')

    item = get_object_or_404(CartItem.objects.using('cart'), id=item_id, cart_id=cart.id)

    action = request.POST.get('action')
    if action == 'increment':
        item.quantity += 1
        item.save(using='cart')
    elif action == 'decrement' and item.quantity > 1:
        item.quantity -= 1
        item.save(using='cart')

    return redirect('cart_view')
