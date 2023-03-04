from django.db import models


class Zoo(models.Model):
    name= models.CharField(max_length= 100)
    city= models.CharField(max_length= 100)
    country= models.CharField(max_length= 100)
    surface= models.DecimalField(max_digits=10, decimal_places= 2)
    budget= models.DecimalField(max_digits=20, decimal_places= 2)


    def __str__(self):
        return self.name



