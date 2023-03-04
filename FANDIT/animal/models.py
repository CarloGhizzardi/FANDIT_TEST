from django.db import models


class Animal(models.Model):
    common_name= models. CharField(max_length= 50, null= False)
    scientific_name= models.CharField(max_length= 100, null= False)
    family_id= models.ForeignKey(Family, on_delete= models.CASCADE, null=False)
    in_extinction= models.BooleanField(default= False, null= False)
    zoo_id= models.ManyToManyField(Zoo)

    def __str__(self):
        return self.common_name

        



