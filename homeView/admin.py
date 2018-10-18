from django.contrib import admin
from .models import HealthData

# Register your models here.


class AdAdmin(admin.ModelAdmin):
    list_display = ['id', 'dateVal']
    list_display_links = ['id', 'ad_title']  # forcing to display id of model
    list_editable = ['status']


admin.site.register(HealthData)
