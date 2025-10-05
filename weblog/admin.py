from django.contrib import admin
from . import models



class prot_title_admin(admin.ModelAdmin):
    list_display=['__str__','is_active']
    list_editable=['is_active']


# Register your models here.
admin.site.register(models.Category,prot_title_admin)
admin.site.register(models.Weblog,prot_title_admin)


