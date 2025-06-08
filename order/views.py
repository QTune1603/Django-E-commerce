from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def order_history(request):
    # (Giả sử bạn có model Order)
    orders = request.user.order_set.all()  # hoặc truy từ Customer model tùy thiết kế
    return render(request, 'order/order_history.html', {'orders': orders})