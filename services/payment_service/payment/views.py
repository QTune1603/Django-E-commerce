from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from services.cart_service.cart.models import Cart, CartItem
from services.customer_service.customer.models import Customer
from services.book_service.book.models import Book
from services.order_service.order.models import Order, OrderItem
from django.db import transaction

@login_required
def payment_home(request):
    user = request.user

    # ✅ Lấy Customer từ DB default
    customer = Customer.objects.using('default').get(user=user)

    # ✅ Lấy cart từ DB cart
    cart = Cart.objects.using('cart').filter(customer=customer.id).first()
    cart_items = CartItem.objects.using('cart').filter(cart=cart)

    # ✅ Lấy sách từ DB default
    book_ids = [item.book_id for item in cart_items]
    books = {b.id: b for b in Book.objects.using('default').filter(id__in=book_ids)}

    for item in cart_items:
        item.book = books.get(item.book_id)
        item.book_price = item.book.price if item.book else 0

    total = sum(item.book_price * item.quantity for item in cart_items)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # ✅ Tạo Order và OrderItem vào DB order
        with transaction.atomic(using='order'):
            order = Order.objects.using('order').create(customer=customer)
            for item in cart_items:

                book_obj = Book.objects.using('default').get(id=item.book_id)
                OrderItem.objects.using('order').create(
                    order=order,
                    book=book_obj,
                    quantity=item.quantity,
                    price=item.book_price
                )

        # ✅ Xoá cart sau khi thanh toán
        cart_items.delete()
        cart.delete()

        return redirect('order_history')

    return render(request, 'payment/home.html', {
        'cart_items': cart_items,
        'total': total
    })
