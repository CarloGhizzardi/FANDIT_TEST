from django.contrib import admin
from zoo.models import Zoo 
from animal.models import Animal
from family.models import Family






    
 

class ZooAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'city', 'country']


admin.site.register(Zoo, ZooAdmin)


