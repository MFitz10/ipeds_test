from django.contrib import admin

from dashboard.models import Affiliation

class AffiliationAdmin(admin.ModelAdmin):
    actions = ['make_onsite', 'make_offsite', 'make_no_affiliation']
    list_display = ('unitid', 'affiliation')
    list_display_links = None
    list_editable = ('affiliation',)
    list_filter = ('affiliation',)
    search_fields = ('unitid__school_name',)

    def make_onsite(self, request, queryset):
        queryset.update(affiliation='onsite')

    def make_offsite(self, request, queryset):
        queryset.update(affiliation='offsite')

    def make_no_affiliation(self, request, queryset):
        queryset.update(affiliation='none')

    make_onsite.short_description = "Mark selected school affiliations as on-campus"
    make_offsite.short_description = "Mark selected school affiliations as virtual"
    make_no_affiliation.short_description = "Mark selected schools as unaffiliated"

admin.site.register(Affiliation, AffiliationAdmin)
