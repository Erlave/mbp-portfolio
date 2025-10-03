from django.contrib import admin
from . import models
# Register your models here.
class contact_admin(admin.ModelAdmin):
    list_display=['__str__','is_read_admin']
    list_editable=['is_read_admin']


admin.site.register(models.contact_model,contact_admin)