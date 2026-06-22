from django import forms

from products.views.products import Category, Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50, required=True, label='Наименование',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наименование товара'})
    )
    price = forms.DecimalField(
        max_digits=7, decimal_places=2, required=True, label='Стоимость',
        widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Cтоимость товара'})
    )
    description = forms.CharField(
        max_length=500, required=True, label='Описание',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    category = forms.ModelChoiceField(
        required=True, queryset=Category.objects.all(), label='Категория',
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категория'})
    )
    image = forms.URLField(
        required=True, label='URL на изображение',
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    remainder = forms.IntegerField(
        min_value=0, required=True, label ='Остаток',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Остаток'} )
    )
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

class SearchForm(forms.Form):
    query = forms.CharField(required=False, label='Поиск по названию')