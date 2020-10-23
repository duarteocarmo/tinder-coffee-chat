from django.db import models
from django.contrib.auth.models import AbstractUser

class Interest(models.Model):
    name = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return f"Interest name: {self.name}"


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    location = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    position = models.CharField(blank=True, max_length=100)
    available = models.BooleanField(default=False)
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return f"email:{self.email}; available: {self.available}"
