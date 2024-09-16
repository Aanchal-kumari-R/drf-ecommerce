from rest_framework import serializers 
from drfecommerce.product.models import (Brand ,Category, Product ,ProductLine) 


class ProductLineSerializer(serializers.ModelSerializer): 
    class Meta: 
         model = ProductLine 
         fields = '__all__' 

class BrandSerializer(serializers.ModelSerializer): 
    class Meta: 
         model = Brand 
         fields = '__all__' 

class CategorySerializer(serializers.ModelSerializer):  
    class Meta: 
         model = Category 
         fields = '__all__' 


class ProductSerializer(serializers.ModelSerializer): 
    brand_name = serializers.CharField(source = "brand.name") 
    category_name = serializers.CharField(source = "category.name") 
    product_line = ProductLineSerializer(many = True) 
    class Meta: 
         model = Product 
         fields = ( 
              "name",
              "desc", 
              "brand_name", 
              "category_name", 
              "product_line",
         ) 
  