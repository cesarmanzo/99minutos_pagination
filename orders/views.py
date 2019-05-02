from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from .models import Orders
from .serializers import OrdersSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer
    permission_classes = ()

    def get_queryset(self):
        return Orders.objects.all()
