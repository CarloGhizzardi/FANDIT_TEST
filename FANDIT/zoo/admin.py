from django.contrib import admin
from zoo.models import Zoo, AnimalRegistration
from animal.models import Animal
from family.models import Family





class AnimalRegistrationInline(admin.TabularInline):
    model = AnimalRegistration
    
 

class ZooAdmin(admin.ModelAdmin):
    inlines=[AnimalRegistrationInline]
    list_display = ['name', 'city', 'country']


admin.site.register(Zoo, ZooAdmin)


