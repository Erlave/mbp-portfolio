from django.contrib import admin
from . import models

# Register your models here.


class portfolio_admin(admin.ModelAdmin):
    list_display=['__str__','is_active']
    list_editable=['is_active']



class prot_title_admin(admin.ModelAdmin):
    list_display=['__str__','is_active']
    list_editable=['is_active']










admin.site.register(models.prot_title,prot_title_admin)
admin.site.register(models.portfolio,portfolio_admin)