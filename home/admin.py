from django.contrib import admin
from . import models
# Register your models here.

class services_admin(admin.ModelAdmin):
    list_display=['__str__','is_active']
    list_editable=['is_active']


class hi_admin(admin.ModelAdmin):
    list_display = [ '__str__','is_active',]
    list_editable = [ 'is_active',]


class home_model_admin(admin.ModelAdmin):
    list_display = [ '__str__','is_active',]
    list_editable = [ 'is_active',]

class my_ability_admin(admin.ModelAdmin):
    list_display = [ '__str__','is_active',]
    list_editable = [ 'is_active',]


class comments_admin(admin.ModelAdmin):
    list_display = [ '__str__','is_active',]
    list_editable = [ 'is_active',]


admin.site.register(models.my_ability,my_ability_admin)
admin.site.register(models.comments,comments_admin)
admin.site.register(models.services,services_admin)
admin.site.register(models.work_area,hi_admin)
admin.site.register(models.home_model,home_model_admin)