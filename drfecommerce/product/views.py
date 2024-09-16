from rest_framework import viewsets 
from rest_framework.response import Response   
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from drfecommerce.product.models import (Brand ,Category, Product)  
from drfecommerce.product.serializers import (ProductSerializer,BrandSerializer,CategorySerializer)

# Create your views here.

class CategoryViewSet(viewsets.ViewSet): 
    serializer_class = CategorySerializer 
    @extend_schema(request=CategorySerializer)  
    def list(self,request): 
        queryset = Category.objects.all() 
        serializer = CategorySerializer(queryset,many=True) 
        return Response(serializer.data)  

class BrandViewSet(viewsets.ViewSet):  
    serializer_class = BrandSerializer  
    @extend_schema(request=BrandSerializer)
    def list(self,request): 
        queryset = Brand.objects.all() 
        serializer = BrandSerializer(queryset,many=True) 
        return Response(serializer.data) 
    
class ProductViewSet(viewsets.ViewSet): 
    queryset = Product.objects.all()  
    
    @action(
            url_path=r"category/(?P<category>[^/]+)/all",  
            methods=['get'], 
             detail=False
    )
    def list_products_by_category(self,request,category=None):  
        serialized = ProductSerializer(self.queryset.filter(category__name=category),many=True) 
        return Response(serialized.data) 
     

    serializer_class = ProductSerializer  
    @extend_schema(request=ProductSerializer)
    def list(self,request): 
        serializer = ProductSerializer(self.queryset,many=True) 
        return Response(serializer.data) 