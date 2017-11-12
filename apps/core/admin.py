from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from apps.core.models import Member, Organization, Location


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Location, MPTTModelAdmin)
