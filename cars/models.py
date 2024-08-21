from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100)
    has_cars = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Car(models.Model):
    COLOR_CHOICES = [
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('gray', 'Gray')
    ]
    MODEL_CHOICES = [
        ('hatch', 'Hatch'),
        ('sedan', 'Sedan'),
        ('convertible', 'Convertible')
    ]
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    model = models.CharField(max_length=20, choices=20)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)