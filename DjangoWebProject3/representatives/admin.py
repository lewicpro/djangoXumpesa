from django.contrib import admin
from representatives.models import Representative, Suggest


def accepted (Modeladmin, request, queryset):
    queryset.update(status='Accepted')


def rejected(modeladmin, request, queryset):
    queryset.update(status='Rejected')


class RepresentativesAdmin(admin.ModelAdmin):
    list_display = ['user', 'names', 'country', 'region', 'phone', 'last_online', 'social_media', 'status']
    # list_editable = ['phone']
    actions = [accepted, rejected]


class SuggestAdmin(admin.ModelAdmin):
    list_display = ["user", "subject", "suggestion", "timestamp"]

admin.site.register(Suggest, SuggestAdmin)
admin.site.register(Representative, RepresentativesAdmin)
