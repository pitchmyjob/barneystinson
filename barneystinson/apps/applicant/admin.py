from django.contrib import admin

from .models import Applicant, Experience, Formation, Skill, Language, Interest


class ExperienceInlineAdmin(admin.TabularInline):
    model = Experience
    fields = ('company', 'position', 'location', 'description')
    extra = 0


class FormationInlineAdmin(admin.TabularInline):
    model = Formation
    fields = ('school', 'degree', 'description')
    extra = 0


class SkillInlineAdmin(admin.TabularInline):
    model = Skill
    fields = ('name', 'level')
    extra = 0


class LanguageInlineAdmin(admin.TabularInline):
    model = Language
    fields = ('name', 'level')
    extra = 0


class InterestInlineAdmin(admin.TabularInline):
    model = Interest
    fields = ('name',)
    extra = 0


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    fields = ('user', 'title', 'birthday', 'description', 'url', 'wanted_skills', 'wanted_jobs', 'wanted_contracts')
    readonly_fields = ('user',)
    filter_horizontal = ('wanted_contracts',)
    list_display = ('user', 'title')
    list_filter = ('wanted_contracts',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'title', 'wanted_skills', 'wanted_jobs')
    inlines = [ExperienceInlineAdmin, FormationInlineAdmin, SkillInlineAdmin, LanguageInlineAdmin, InterestInlineAdmin]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
