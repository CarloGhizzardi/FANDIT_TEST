from django.db import models
from animal.models import Animal



class Zoo(models.Model):
    name= models.CharField(max_length= 100)
    city= models.CharField(max_length= 100)
    country= models.CharField(max_length= 100)
    surface= models.DecimalField(max_digits=10, decimal_places= 2, help_text='m2')
    budget= models.DecimalField(max_digits=20, decimal_places= 2, help_text='Anual')
    animals= models.ManyToManyField(Animal)
    
    
    def __str__(self):
        return self.name


class ZooAnimal(models.Model):
    