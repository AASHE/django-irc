from django.contrib import admin
from rc.resources.admin import ResourceItemAdmin
from rc.resources.apps.pae.models import *


admin.site.register(AssessmentTool, ResourceItemAdmin)
admin.site.register(MasterPlan, ResourceItemAdmin)
admin.site.register(SustainabilityWebsite, ResourceItemAdmin)
admin.site.register(SustainabilityBlog, ResourceItemAdmin)
admin.site.register(SustainabilityPlan, ResourceItemAdmin)
admin.site.register(AlumniFund, ResourceItemAdmin)
admin.site.register(RevolvingLoanFund, ResourceItemAdmin)
admin.site.register(StudentFee, ResourceItemAdmin)
