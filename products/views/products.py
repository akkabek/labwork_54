from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from products.models import Product, Category
from products.forms import ProductForm


class ProductListView(ListView):
    template_name = 'products/product_list.html'
    model = Product
    paginate_by = 5
    context_object_name = 'products'

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        if query:
            qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_view.html', {'product': product})

def category_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        if name:
            Category.objects.create(
                name=name,
                description=description)
        return redirect('product_list')
    return render(request, 'categories/category_add_view.html')

def product_add_view(request):
    if request.method == 'GET':
        product_form = ProductForm()
        return render(request, 'products/product_add_view.html', {'form': product_form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                price=form.cleaned_data['price'],
                image=form.cleaned_data['image'],
                remainder=form.cleaned_data['remainder'],
            )
            return redirect('product_list')
        else:
            return render(request, 'products/product_add_view.html', context={'form': form})

def product_edit_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request, 'products/product_edit_view.html', {'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.price = form.cleaned_data['price']
            product.image = form.cleaned_data['image']
            product.remainder = form.cleaned_data['remainder']
            product.save()
            return redirect('product_list')
        else:
            return render(request, 'products/product_add_view.html', context={'form': form})


def product_delete_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        return render(request, 'products/product_delete_view.html', {'product': product})
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return redirect('product_view', id=id)