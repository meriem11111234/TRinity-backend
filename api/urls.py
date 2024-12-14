from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, InvoiceViewSet
from .views import OpenFoodFactsProductView, KPIView,RegisterView

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('products', ProductViewSet, basename='product')
router.register('invoices', InvoiceViewSet, basename='invoice')

urlpatterns = [
    path('', include(router.urls)),
    path('products/openfoodfacts/<str:barcode>/', OpenFoodFactsProductView.as_view(), name='fetch_openfoodfacts_product'),
    path('reports/', KPIView.as_view(), name='kpi_view'),
    path('api/register/', RegisterView.as_view(), name='register'),
]
