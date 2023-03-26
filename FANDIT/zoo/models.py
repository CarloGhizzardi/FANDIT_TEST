from django.db import models
from animal.models import Animal

class Zoo(models.Model):
    name= models.CharField(max_length= 100)
    city= models.CharField(max_length= 100)
    country= models.CharField(max_length= 100)
    surface= models.DecimalField(max_digits=10, decimal_places= 2, help_text='m2')
    budget= models.DecimalField(max_digits=20, decimal_places= 2, help_text='Anual')
    animals= models.ManyToManyField(Animal, through= 'ZooAnimal', blank=True)

    class Meta:
        ordering= ['country', 'city', 'name']
    
    def __str__(self):
        return self.name
    

class ZooAnimal(models.Model):
    zoo= models.ForeignKey(Zoo, on_delete=models.CASCADE, blank=True, null=True)
    animal= models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name= 'animal Zoo'
        verbose_name_plural= 'animales Zoos'

    def __str__(self):
        return str(self.id)