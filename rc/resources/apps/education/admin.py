from django.contrib import admin
from rc.resources.admin import ResourceItemAdmin
from rc.resources.apps.education.models import *


admin.site.register(CommunityGarden, ResourceItemAdmin)
admin.site.register(SustainabilityNetworks, ResourceItemAdmin)
admin.site.register(CampusAgriculture, ResourceItemAdmin)
admin.site.register(LivingGuides, ResourceItemAdmin)
admin.site.register(SustainabilityMaps, ResourceItemAdmin)
admin.site.register(StudentPeerOutreach, ResourceItemAdmin)
admin.site.register(CampusSustainabilityCourse, ResourceItemAdmin)
admin.site.register(SustainabilityCourseInventory, ResourceItemAdmin)
admin.site.register(SustainabilitySyllabus, ResourceItemAdmin)
admin.site.register(FacultyWorkshops, ResourceItemAdmin)
admin.site.register(SurveyOfAwareness, ResourceItemAdmin)
admin.site.register(ResearchInventories, ResourceItemAdmin)
admin.site.register(AcademicCenter, ResourceItemAdmin)
admin.site.register(AcademicCenterType)
