from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=255)

class Shoe(models.Model):
    model = models.CharField(max_length=255)
    release_date = models.DateField()
    color = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=255, blank=True, null=True)