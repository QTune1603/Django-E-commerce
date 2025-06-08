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
    path('payment/', include('payment.urls')),   # ✅ sửa import và include
    path('cart/', include('cart.urls')),
    path('customer/', include('customer.urls')),
    path('order/', include('order.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
