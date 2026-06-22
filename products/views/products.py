from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.urls import reverse_lazy

from products.models import Product, Category
from products.forms import ProductForm


class ProductListView(ListView):
    template_name = 'products/product_list.html'
    model = Product
    paginate_by = 5
    context_object_name = 'products'

    def get_queryset(self):
        qs = Product.objects.filter(remainder__gte=1).order_by('category__name', 'name')
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['categories'] = Category.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_view.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_add_view.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_edit_view.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete_view.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product'