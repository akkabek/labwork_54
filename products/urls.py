from django.urls import path
from . import views
from products.views import (ProductListView, ProductDetailView, ProductCreateView,
                            ProductUpdateView, ProductDeleteView)
from products.views import CartListView, CartAddView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product_view'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/<int:id>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:id>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('categories/add/', views.category_add_view, name='category_add'),
    path('categories/', views.categories_view, name='categories_view'),
    path('categories/<int:id>/edit/', views.category_edit_view, name='category_edit'),
    path('categories/<int:id>/delete/', views.category_delete_view, name='category_delete'),
    path('products/<slug:slug>/', views.category_products_view, name='category_products'),

    path('cart/', CartListView.as_view(), name='cart'),
    path('cart/add/<int:pk>/', CartAddView.as_view(), name='cart_add'),
]