from django.db import models
from family.models import Family
from zoo.models import Zoo



class Animal(models.Model):
    common_name= models. CharField(max_length= 50, null= False)
    scientific_name= models.CharField(max_length= 100, null= False)
    family_id= models.ForeignKey(Family, on_delete= models.CASCADE, null=False)
    in_extinction= models.BooleanField(default= False, null= False)
    
    def __str__(self):
        return self.common_name

        



