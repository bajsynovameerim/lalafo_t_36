from django import forms
from .models import Product


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'category', 'product_image',
                  'phone_number', 'descriptions', 'city', 'user']
        labels = {
            'product_name': 'Название',
            'price': 'Цена, сом',
            'category': 'Категория',
            'product_image': 'Фото товара',
            'phone_number': 'Телефон',
            'descriptions': 'Описание',
            'city': 'Город',
            'user': 'Ваше имя',
        }
        widgets = {
            'product_name': forms.TextInput(attrs={'placeholder': 'Например, Футболка'}),
            'price': forms.NumberInput(attrs={'placeholder': '1500'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+996555123456'}),
            'descriptions': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Расскажите о товаре'}),
            'city': forms.TextInput(attrs={'placeholder': 'Бишкек'}),
            'user': forms.TextInput(attrs={'placeholder': 'Как к вам обращаться'}),
        }