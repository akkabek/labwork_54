from django.shortcuts import render, get_object_or_404, redirect

from products.models import Product, Category

def products_view(request):
    products = Product.objects.all().filter(remainder__gte=1).order_by('category').order_by('name')
    return render(request, 'products_view.html', {'products': products})

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
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        category_id = request.POST.get('category', '').strip()
        price = request.POST.get('price', '').strip()
        image = request.POST.get('image', '').strip()
        remainder = request.POST.get('remainder', '').strip()
        if name and category_id:
            category = get_object_or_404(Category, id=category_id)
            new_product = Product.objects.create(
                name=name,
                description=description,
                category=category,
                price=price,
                image=image,
                remainder=remainder
            )
            return redirect('product_view', id=new_product.id)
    return render(request,'product_add_view.html', {'categories': categories})

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