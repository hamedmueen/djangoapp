from django.db import models

# Create your models here.
class food(models.Model):
    name = models.CharField(max_length=50)
    calories = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.URLField()
