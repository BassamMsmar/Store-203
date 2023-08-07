<<<<<<< HEAD
from django import forms

from .models import Product ,Brand ,SubCategory, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
=======
from django import forms

from .models import Product ,Brand ,SubCategory, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
>>>>>>> 58893b5 (fix error template not exit)
        fields = '__all__'