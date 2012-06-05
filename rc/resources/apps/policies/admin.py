from django.contrib import admin
from rc.resources.apps.policies.models import *


class PolicyAdmin(admin.ModelAdmin):
    list_filter = ('type', 'published')
    list_display = ('__unicode__', 'organization', 'published', 'type')
admin.site.register(Policy, PolicyAdmin)
admin.site.register(GreenBuildingPolicy, PolicyAdmin)
admin.site.register(ResponsibleInvestmentPolicy, PolicyAdmin)
admin.site.register(FairTradePolicy, PolicyAdmin)

class PolicyTypeAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'type')
    list_editable = ['type']
admin.site.register(PolicyType, PolicyTypeAdmin)
