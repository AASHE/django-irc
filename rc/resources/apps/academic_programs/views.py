from django.http import Http404
from django.core.urlresolvers import reverse 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from aashe.disciplines.models import Discipline
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.edit import CreateView, UpdateView, FormView
from haystack.views import SearchView, search_view_factory
from rc.resources.apps.academic_programs.models import *
from rc.resources.apps.academic_programs.forms import *
from django.core.paginator import InvalidPage, EmptyPage #, Paginator
from rc.resources.apps.academic_programs.digg_paginator import DiggPaginator as Paginator

class ProgramList(ListView):
    allow_empty = True
    model = AcademicProgram
    paginate_by = 50
    
class ProgramMap(ListView):
    queryset = AcademicProgram.objects.filter(published=True)
    
class ProgramIndex(ListView):
    queryset = AcademicProgram.objects.filter(published=True)
            
    def get_context_data(self, **kwargs):
        context = super(ProgramIndex, self).get_context_data(**kwargs)
        # Check if disciplines have programs
        disciplines = Discipline.objects.all()
        final_disciplines = []
        for discipline in disciplines:
          program_count = AcademicProgram.objects.filter(discipline=discipline).count()
          if program_count > 0:
            final_disciplines.append(discipline)
          else:
            pass
        
        # Add disciplines to context
        context['disciplines'] = final_disciplines
        
        # Check if types have programs
        program_types = ProgramType.objects.all()
        final_types = []
        for program_type in program_types:
          program_count = AcademicProgram.objects.filter(program_type=program_type).count()
          if program_count > 0:
            final_types.append(program_type)
          else:
            pass
        # Add program types to context
        context['types'] = final_types
        
        context['total_programs'] = AcademicProgram.objects.filter(published=True).count()
        context['total_campuses'] = AcademicProgram.objects.filter(published=True).values('institution').distinct().count()
        context['total_states'] = AcademicProgram.objects.filter(published=True).values('state').distinct().count()
        
        return context

class ProgramTypeTable(ListView):    
    def get_queryset(self):
        if self.context_object_name == 'program_type':
            self.program_type = get_object_or_404(ProgramType, slug=self.kwargs['type'])
            return AcademicProgram.objects.filter(program_type=self.program_type)
    
    def get_context_data(self, **kwargs):
        context = super(ProgramTypeTable, self).get_context_data(**kwargs)
        try:
          context['program_type'] = ProgramType.objects.get(slug=self.kwargs['type']).name
          context['count'] = AcademicProgram.objects.filter(program_type=self.program_type).count()
          return context
        except:
          return context
      
class ProgramDisciplineTable(ListView):
  def get_queryset(self):
      if self.context_object_name == 'discipline':
          self.discipline = get_object_or_404(Discipline, slug=self.kwargs['discipline'])
          return AcademicProgram.objects.filter(discipline=self.discipline)
  
  def get_context_data(self, **kwargs):
      context = super(ProgramDisciplineTable, self).get_context_data(**kwargs)
      try:
        context['discipline'] = Discipline.objects.get(slug=self.kwargs['discipline']).name
        context['count'] = AcademicProgram.objects.filter(discipline=self.discipline).count()
        return context
      except:
        return context

class ProgramDetail(DetailView):
    queryset = AcademicProgram.objects.filter(published=True)
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ProgramDetail, self).get_context_data(**kwargs)
        return context
        
# CRUD Views
class ProgramCreateView(CreateView):
    form_class = ProgramCreateForm
    template_name = 'academic_programs/ap_create.html'

    def get_form(self, form_class):
        form = form_class(**self.get_form_kwargs())
        form.request = self.request
        return form

    def get_success_url(self):
        return reverse("program-add-success")

class ProgramUpdateView(UpdateView):
    model = AcademicProgram
    form_class = ProgramUpdateForm
    template_name = 'academic_programs/ap_update.html'

    def get_success_url(self):
        return reverse("program-edit-success")

    def get_form(self, form_class):
        form = form_class(**self.get_form_kwargs())
        form.request = self.request
        return form

# Overridden search views
class ProgramSearchView(SearchView):
    def build_page(self):
        """
        Paginates the results appropriately.

        In case someone does not want to use Django's built-in pagination, it
        should be a simple matter to override this method to do what they would
        like.
        """
        try:
            page_no = int(self.request.GET.get('page', 1))
        except (TypeError, ValueError):
            raise Http404("Not a valid number for page.")

        if page_no < 1:
            raise Http404("Pages should be 1 or greater.")

        start_offset = (page_no - 1) * self.results_per_page
        self.results[start_offset:start_offset + self.results_per_page]

        paginator = Paginator(self.results, self.results_per_page)

        try:
            page = paginator.page(page_no)
        except InvalidPage:
            raise Http404("No such page!")

        return (paginator, page)