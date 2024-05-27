from rest_framework import viewsets, generics
from .models import Stock, StockPrice
from .serializers import StockSerializer, StockPriceSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockPriceViewSet(viewsets.ModelViewSet):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer

class StockCreateView(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockUpdateView(generics.UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDeleteView(generics.DestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer