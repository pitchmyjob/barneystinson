from django.contrib import admin

from .models import Pro


@admin.register(Pro)
class ProAdmin(admin.ModelAdmin):
    fields = ('company', 'logo', 'industry', 'employes', 'ca', 'phone', 'website', 'description')
    list_display = ('company', 'industry', 'employes', 'ca', 'phone', 'website')
    search_fields = ('company', 'description')
