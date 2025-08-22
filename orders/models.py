from django.db import models
from users.models import User

class Order(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["user"])]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} (user_id={self.user_id})"

