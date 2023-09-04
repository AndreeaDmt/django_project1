from django.contrib import admin
from . models import Book, Order, OrderItem


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Order)

admin.site.register(OrderItem)