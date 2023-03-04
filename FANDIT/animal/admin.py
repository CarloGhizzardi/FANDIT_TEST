from django.contrib import admin
from animal.models import animal

class AnimalAdmin(admin.ModelAdmin):
    list_display=['common_name', 'family']
