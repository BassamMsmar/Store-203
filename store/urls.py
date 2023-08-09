from django.urls import path

from .views import  CreateBrand ,CreateSubCategory, CreateCategory, products, product_details ,add_product, product_delete, edit_product
urlpatterns = [
    # path('', index, name='index'),
    path('products/', products, name='products'),
    path('details/<int:pk>/', product_details, name='product_details'),
    path('edit/<int:pk>/', edit_product, name='edit_product'),
    path('delete/<int:pk>/', product_delete, name='product_delete'),
    path('add/product/', add_product, name='add_product'),
    path('add/category/', CreateCategory.as_view(), name='CreateCategory'),
    path('add/sub_category/', CreateSubCategory.as_view(), name='CreateSubCategory'),
    path('add/brand/', CreateBrand.as_view(), name='CreateBrand'),
]