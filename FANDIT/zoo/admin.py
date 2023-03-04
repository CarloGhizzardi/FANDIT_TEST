from django.contrib import admin
from zoo.models import Zoo

@admin.register(Zoo)
class ZooAdmin(admin.ModelAdmin):
    list_display=['name', 'city', 'country']

