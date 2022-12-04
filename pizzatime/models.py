from django.db import models

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=40, unique=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Pizza(models.Model):
    specialty = models.CharField(max_length=40, unique=True)
    toppings = models.ManyToManyField(Topping)

    class Meta:
        ordering = ['specialty']

    def __str__(self):
        return self.specialty