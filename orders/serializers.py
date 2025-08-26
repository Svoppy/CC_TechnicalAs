from rest_framework import serializers
from .models import Order
from users.models import User

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Order
        fields = ["id", "title", "description", "user","created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def to_representation(self, instance):
        from users.serializers import UserSerializer
        representation = super().to_representation(instance)

        representation['user'] = UserSerializer(instance.user).data
        return representation
        