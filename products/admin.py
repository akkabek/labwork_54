from django.contrib import admin
from .models import Category, Product, Order

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category','price', 'remainder', 'created_at']
    list_filter = ['category', 'name', 'created_at']
    search_fields = ['name', 'category__name']
    fields = [ 'name','description', 'category', 'price','remainder', 'image']
    readonly_fields = ['created_at']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','phone','created_at']
    ordering =['-created_at']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)