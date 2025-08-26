from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
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

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["user"]
    search_fields = ["description"]
    ordering_fields = ["created_at"]