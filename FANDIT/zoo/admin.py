from django.contrib import admin
from zoo.models import Zoo 
from animal.models import Animal
from family.models import Family






    

@admin.register(Zoo)
class ZooAdmin(admin.ModelAdmin):
    pass





