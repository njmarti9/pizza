from django.db import models

# Toppings have 1 string = name
class Topping(models.Model):
    name = models.CharField(max_length=40, unique=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Pizza has 1 string = name, and 1 list of toppings
class Pizza(models.Model):
    specialty = models.CharField(max_length=40, unique=True)
    toppings = models.ManyToManyField(Topping)

    class Meta:
        ordering = ['specialty']

    def __str__(self):
        return self.specialty