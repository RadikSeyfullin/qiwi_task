from django.shortcuts import render
from order.models import Order
from rest_framework import viewsets
from order.serializers import OrderSerializer

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
