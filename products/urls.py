from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name='products'),
    path('products/', views.products_view, name='products_list'),
    path('products/<int:id>/', views.product_view, name='product_view'),
    path('products/add/', views.product_add_view, name='product_add'),
    path('products/<int:id>/edit/', views.product_edit_view, name='product_edit'),
    path('products/<int:id>/delete/', views.product_delete_view, name='product_delete'),
    path('categories/add/', views.category_add_view, name='category_add'),
    path('categories/', views.categories_view, name='categories_view'),
    path('categories/<int:id>/edit/', views.category_edit_view, name='category_edit'),
    path('categories/<int:id>/delete/', views.category_delete_view, name='category_delete'),
    path('products/<slug:slug>/', views.category_products_view, name='category_products'),
]