from django.contrib import admin

from .models import Industry, Employee, ContractType, Experience, StudyLevel


class DataAdmin(object):
    fields = ('name', 'is_active', 'order')
    list_display = ('name', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(Industry)
class IndustryAdmin(DataAdmin, admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(DataAdmin, admin.ModelAdmin):
    pass


@admin.register(ContractType)
class ContractTypeAdmin(DataAdmin, admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(DataAdmin, admin.ModelAdmin):
    pass


@admin.register(StudyLevel)
class StudyLevelAdmin(DataAdmin, admin.ModelAdmin):
    pass
