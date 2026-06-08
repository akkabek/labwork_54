from django.contrib import admin
from .models import Category,Product

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category','price', 'remainder', 'created_at']
    list_filter = ['category', 'name', 'created_at']
    search_fields = ['name', 'category']
    fields = [ 'name','description', 'category', 'price','remainder', 'created_at']
    readonly_fields = ['created_at']

admin.site.register(Product, ProductAdmin)