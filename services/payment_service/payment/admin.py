from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount', 'timestamp', 'payment_method', 'payment_status')
    list_filter = ('payment_status', 'payment_method')
    search_fields = ('order__id', 'transaction_id')
