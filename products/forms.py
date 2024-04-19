from products.models import Product
from django import forms
from products import models

class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['title', 'content', 'price']

    def clean(self):
        self.cleaned_data['author'] = self.author
        return self.cleaned_data

    def save(self, author):
        product_instance = super().save(commit=False)
        product_instance.author = author
        product_instance.save()
        return product_instance


def __init__(self, *args, **kwargs):
    self.author = kwargs.pop("author")
    super().__init__(*args, **kwargs)




