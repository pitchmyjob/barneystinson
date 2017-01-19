from django.contrib import admin

from .filters import StateListFilter
from .models import Job, JobQuestion


class JobQuestionInlineAdmin(admin.TabularInline):
    model = JobQuestion
    fields = ('job', 'question', 'order')
    extra = 0


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    fields = ('pro', 'title', 'contract_types', 'experiences', 'study_levels', 'salary', 'skills', 'description',
              'view_counter', 'last_payment', 'is_active')
    filter_horizontal = ('contract_types', 'experiences', 'study_levels')
    list_display = ('pro', 'title', 'is_active', 'get_state', 'last_payment')
    list_filter = (StateListFilter, 'is_active', 'contract_types', 'experiences', 'study_levels')
    search_fields = ('title', 'skills', 'description')
    inlines = [JobQuestionInlineAdmin]
