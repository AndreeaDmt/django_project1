from django.contrib import admin
from . models import Book, User, Order

# Register your models here.

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):

#     prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(User)

admin.site.register(Order)