from rest_framework import viewsets, mixins
from .models import User
from .serializers import UserSerializer

class UserViewSet(mixins.CreateModelsMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookuo_field = "id"