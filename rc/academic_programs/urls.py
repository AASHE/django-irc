from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from rc.academic_programs.models import AcademicProgram
from rc.academic_programs.views import StudyList

# Create your views here.
urlpatterns = patterns('',
    url(r'^resources/academic-programs/search$', StudyList.as_view(
            template_name='academic-programs/ac_browse.html'),
))