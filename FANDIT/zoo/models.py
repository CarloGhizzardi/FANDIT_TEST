from django.db import models
from animal.models import Animal
from family.models import Family


class Zoo(models.Model):
    name= models.CharField(max_length= 100)
    city= models.CharField(max_length= 100)
    country= models.CharField(max_length= 100)
    surface= models.DecimalField(max_digits=10, decimal_places= 2)
    budget= models.DecimalField(max_digits=20, decimal_places= 2)
    registeredAnimal= models.ManyToManyField(Animal, through='AnimalRegistration')


    def __str__(self):
        return self.name

class AnimalRegistration(models.Model):
    zoo_id= models.ForeignKey(Zoo, on_delete= models.CASCADE)
    animal_id= models.ForeignKey(Animal, on_delete= models.CASCADE)
    family_id= models.ForeignKey(Family, on_delete= models.CASCADE)
    class Meta:
        ordering = ["family_id"]




