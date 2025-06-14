from django.contrib import admin
from django.urls import path, include
from qtung_project1.views import home_view
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Trang mặc định chuyển hướng đến login
    path('', lambda request: redirect('login')),

    # Trang chính
    path('home/', home_view, name='home'),

    # Các app chính
    path('home/<str:category>/', home_view, name='book_category'),
    path('payment/', include('services.payment_service.payment.urls')),   # ✅ sửa import và include
    path('cart/', include('services.cart_service.cart.urls')),
    path('customer/', include('services.customer_service.customer.urls')),
    path('order/', include('services.order_service.order.urls')),
    path('accounts/', include('services.accounts_service.accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
