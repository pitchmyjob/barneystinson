from django.contrib import admin

from .models import CandidacyMessage


@admin.register(CandidacyMessage)
class CandidacyMessageAdmin(admin.ModelAdmin):
    fields = ('candidacy', 'emmiter', 'message', 'created')
    readonly_fields = ('created',)
    list_display = ('candidacy', 'emmiter', 'created')
