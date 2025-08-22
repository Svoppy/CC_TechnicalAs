from rest_framework import viewsets, mixins
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.select_related("user").all()
    serializer_class = OrderSerializer
    lookup_field = "id"

