from django.urls import path, include
from rest_framework import routers
from .views import StockViewSet, StockPriceViewSet, StockCreateView, StockUpdateView, StockDeleteView
from django.urls import path


router = routers.DefaultRouter()
router.register(r'stocks', StockViewSet)
router.register(r'stock-prices', StockPriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stocks/create/', StockCreateView.as_view(), name='stock-create'),
    path('stocks/<int:pk>/update/', StockUpdateView.as_view(), name='stock-update'),
    path('stocks/<int:pk>/delete/', StockDeleteView.as_view(), name='stock-delete'),
]