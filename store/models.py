from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='category', null=True)

    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    name = models.CharField(max_length=50, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='images/')
    availability = models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products",null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="Brand_Product",null=True)

    def __str__(self):
        return self.name
    


    
