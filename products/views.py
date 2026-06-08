from django.shortcuts import render, get_object_or_404, redirect

from products.models import Product, Category
from products.forms import SearchForm, ProductForm


def products_view(request):
    products = Product.objects.all().filter(remainder__gte=1).order_by('category').order_by('name')
    search_form = SearchForm(data=request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        if query:
            products = products.filter(name__icontains=query)

    context = {'products': products, 'search_form': search_form}

    return render(request, 'products_view.html', context)

def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_view.html', {'product': product})

def category_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        if name:
            Category.objects.create(
                name=name,
                description=description)
        return redirect('products_list')
    return render(request,'category_add_view.html')

def product_add_view(request):
    if request.method == 'GET':
        product_form = ProductForm()
        return render(request, 'product_add_view.html', {'form': product_form})
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
            return redirect('products_list')
        else:
            return render(request, 'product_add_view.html', context={'form': form})

def product_edit_view(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()
    if request.method == 'POST':
        product.name = request.POST.get('name', '').strip()
        product.description = request.POST.get('description', '').strip()
        product.price = request.POST.get('price', '').strip()
        product.image = request.POST.get('image', '').strip()
        category_id = request.POST.get('category')
        product.category = get_object_or_404(Category, id=category_id)
        product.save()
        return redirect('product_view', id=product.id)
    return render(request,'product_edit_view.html',{'product': product,'categories': categories})

def product_delete_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        return render(request, 'product_delete_view.html', {'product': product})
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return redirect('product_view', id=id)

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories_view.html', {'categories': categories})

def category_edit_view(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.name = request.POST.get('name', '').strip()
        category.description = request.POST.get('description', '').strip()
        category.save()
        return redirect('categories_view')
    return render(request, 'category_edit_view.html', {'category': category})

def category_delete_view(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        category.delete()
    return redirect('categories_view')