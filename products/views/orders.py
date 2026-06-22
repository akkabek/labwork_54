from django.urls import reverse_lazy
from django.views.generic import CreateView

from products.models import Order, OrderItem, CartItem
from products.forms import OrderForm


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        cart_items = CartItem.objects.select_related('product')

        for item in cart_items:
            OrderItem.objects.create(order=self.object,product=item.product,quantity=item.quantity)

        cart_items.delete()
        return response