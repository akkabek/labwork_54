from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование')
    description = models.TextField(max_length=500, null=True, blank=True ,verbose_name='Описание')
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Категории'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=500, null=True, blank=True,verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    image = models.URLField()
    remainder = models.PositiveIntegerField()
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Товары'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'