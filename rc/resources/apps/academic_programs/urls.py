from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from rc.resources.apps.academic_programs.models import AcademicProgram
from rc.resources.apps.academic_programs.views import *
from rc.resources.apps.academic_programs.forms import ProgramsSearchForm
from haystack.views import search_view_factory
from haystack.query import SearchQuerySet

# Create your views here.
urlpatterns = patterns('',
  # CRUD URLs
  url(r'^add/success/$', TemplateView.as_view(
          template_name='academic_programs/ap_crud_success.html'),
      name='program-add-success'),
  url(r'^add/$', login_required()(ProgramCreateView.as_view()),
      name="program-add"),
  url(r'^edit/success/$', TemplateView.as_view(
          template_name='academic_programs/ap_crud_success.html'),
      name='program-edit-success'),    
  url(r'^edit/(?P<slug>[-\w]+)/$', login_required()(ProgramUpdateView.as_view()),
      name="program-edit"),
  url(r'^edit/success/$', 'django.views.generic.base.TemplateView',
      {'template_name': 'academic_programs/ap_crud_success.html'},
      name='program-edit-success'),

  url(r'^type/(?P<type>.*)/$', ProgramTypeTable.as_view(template_name = 'academic_programs/ap_table.html', 
    context_object_name='program_type'), name="program-type-view"),
    
  url(r'^discipline/(?P<discipline>.*)/$', ProgramDisciplineTable.as_view(template_name = 'academic_programs/ap_table.html', 
    context_object_name='discipline'), name="program-discipline-view"),
    
  url(r'^$', ProgramIndex.as_view(
        template_name = 'academic_programs/ap_index.html',
        queryset=AcademicProgram.objects.all()), name="program-index-view"),
        
  url(r'^browse/$', ProgramList.as_view(
            template_name='academic_programs/ap_browse.html')),
            
  url(r'^search/$', search_view_factory(
            view_class=ProgramSearchView,
            template='academic_programs/ap_search.html',
            form_class=ProgramsSearchForm,
            searchqueryset=SearchQuerySet().models(AcademicProgram)),
       name='academic-program-search'),
  url(r'^map/$', ProgramMap.as_view(
             template_name='academic_programs/ap_map.html')),
  url(r'^(?P<slug>[-\w]+)/$', ProgramDetail.as_view(template_name = 'academic_programs/ap_detail.html'), 
   name="program-detail-view"),
   
  

        )