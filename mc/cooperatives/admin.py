from django.contrib import admin
from cooperatives.models import Organization, Cooperative, Partner

class PartnerInline(admin.StackedInline):
    model = Partner
    extra = 1

class CooperativeAdmin(admin.ModelAdmin):
    inlines = [PartnerInline]

admin.site.register(Cooperative, CooperativeAdmin)

admin.site.register(Organization)