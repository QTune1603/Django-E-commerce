from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'is_bestseller', 'is_featured')
    search_fields = ('title',)
    list_filter = ('is_bestseller', 'is_featured')
