from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'