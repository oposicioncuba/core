from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from apps.core.models import Member, Organization, Location


class MemberInline(admin.StackedInline):
    model = Member
    fields = ('name', 'last_name', 'verified')


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [MemberInline]


admin.site.register(Location, MPTTModelAdmin)
