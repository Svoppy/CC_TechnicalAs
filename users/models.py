from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

class User(models.model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True, db_index=True)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["email"])]
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.name} <{self.email}>"
    