from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from products.models import Product, CartItem
from products.forms import OrderForm

class CartListView(ListView):
    template_name = 'cart/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartItem.objects.select_related('product').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = context['cart_items']
        context['total'] = sum(item.total() for item in items)
        context['order_form'] = OrderForm()
        return context

class CartAddView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if product.remainder < 1:
            return redirect('product_list')

        cart_item = CartItem.objects.filter(product=product).first()

        if cart_item is None:
            CartItem.objects.create(product=product, quantity=1)
        else:
            if cart_item.quantity < product.remainder:
                cart_item.quantity += 1
                cart_item.save()

        return redirect('product_list')

class CartRemoveView(View):
    def get(self, request, pk):
        cart_item = get_object_or_404(CartItem, pk=pk)
        cart_item.delete()
        return redirect('cart')