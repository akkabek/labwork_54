from django.shortcuts import render, get_object_or_404, redirect

from products.models import Product, Category
from products.forms import SearchForm

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories_view.html', {'categories': categories})

def category_edit_view(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.name = request.POST.get('name', '').strip()
        category.description = request.POST.get('description', '').strip()
        category.save()
        return redirect('categories_view')
    return render(request, 'categories/category_edit_view.html', {'category': category})

def category_delete_view(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        category.delete()
    return redirect('categories_view')

def category_products_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, remainder__gte=1).order_by('name')

    search_form = SearchForm(data=request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        if query:
            products = products.filter(name__icontains=query)

    context = {
        'products': products,
        'search_form': search_form,
        'category': category,
    }
    return render(request, 'categories/category_products_view.html', context)