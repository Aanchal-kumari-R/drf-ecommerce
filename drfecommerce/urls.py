from django.contrib import admin
from django.urls import path , include 
from rest_framework.routers import DefaultRouter  
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drfecommerce.product.views import (ProductViewSet,BrandViewSet,CategoryViewSet)  


router = DefaultRouter() 
router.register(r'brand/',BrandViewSet,basename="brand")
router.register(r'product/',ProductViewSet,basename="product")
router.register(r'category/',CategoryViewSet,basename="category")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), 
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),


]
