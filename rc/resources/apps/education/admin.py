from django.contrib import admin
from rc.resources.admin import ResourceItemAdmin
from rc.resources.apps.education.models import *


admin.site.register(CommunityGarden, ResourceItemAdmin)
admin.site.register(SustainabilityNetwork, ResourceItemAdmin)
admin.site.register(CampusAgriculture, ResourceItemAdmin)
admin.site.register(LivingGuide, ResourceItemAdmin)
admin.site.register(SustainabilityMap, ResourceItemAdmin)
admin.site.register(StudentPeerOutreach, ResourceItemAdmin)
admin.site.register(CampusSustainabilityCourse, ResourceItemAdmin)
admin.site.register(CampusSustainabilityCourseTeacher)
admin.site.register(SustainabilityCourseInventory, ResourceItemAdmin)
admin.site.register(SustainabilitySyllabus, ResourceItemAdmin)
admin.site.register(FacultyWorkshop, ResourceItemAdmin)
admin.site.register(SurveyOfAwareness, ResourceItemAdmin)
admin.site.register(ResearchInventory, ResourceItemAdmin)
admin.site.register(AcademicCenter, ResourceItemAdmin)
admin.site.register(AcademicCenterType)
