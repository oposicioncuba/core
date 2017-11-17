from django.contrib import admin
from django.contrib.admin import ModelAdmin
from mptt.admin import MPTTModelAdmin

from apps.core.models import Organization, Location, Member


@admin.register(Member)
class MemberAdmin(ModelAdmin):
    list_display = ['name', 'last_name', 'verified']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Location, MPTTModelAdmin)
