from django.contrib import admin
from django.urls import include, path
from qtung_project1.views import home_view
from payment.views import payment_home  # ✅ Add this if the payment app exists
from cart.views import cart_view  # ✅ Add this if the cart app exists
from customer.views import customer_profile  # ✅ Add customer profile
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),
    path('home/', home_view, name='home'),  # ✅ Fix the 'home' URL
    path('payment/', payment_home, name='payment_home'),  # ✅ Fix 'payment_home'
    path('', include('cart.urls')),  # ✅ Fix 'cart_view'
    path('customer/profile/', customer_profile, name='customer_profile'),  # ✅ Fix 'customer_profile'
    
    path('accounts/', include('accounts.urls')),
    path('customer/', include('customer.urls')),
]
