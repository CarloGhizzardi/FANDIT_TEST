from django.contrib import admin
from zoo.models import Zoo,ZooAnimal

    
class ZooAnimalInline(admin.TabularInline):
    model= ZooAnimal
    extra= 1
    

class ZooAdmin(admin.ModelAdmin):
    inlines= [ZooAnimalInline,]
    list_display= ('name', 'country', 'city')


    def presentation(self, obj):
        return obj.name
    
    #search_fields= ('name')
    #list_filter= ('animals')

    filter_horizontal= ['animals']

admin.site.register(Zoo, ZooAdmin)









