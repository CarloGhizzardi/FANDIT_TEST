from django.contrib import admin
from family.models import Family

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display=['name']