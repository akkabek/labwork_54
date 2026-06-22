from django import forms

from products.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'category',
            'image',
            'remainder',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наименование товара'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cтоимость товара'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category':forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категория'}),
            'image':forms.URLInput(attrs={'class': 'form-control'}),
            'remainder':forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Остаток'}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(required=False, label='Поиск по названию')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }