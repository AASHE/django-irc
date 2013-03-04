from django.http import Http404
from django.core.urlresolvers import reverse 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from aashe.disciplines.models import Discipline
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.edit import CreateView, UpdateView, FormView
from haystack.views import SearchView, search_view_factory
from rc.resources.apps.greenfunds.models import *
from rc.resources.apps.greenfunds.forms import *
from django.core.paginator import InvalidPage, EmptyPage #, Paginator
from rc.resources.apps.academic_programs.digg_paginator import DiggPaginator as Paginator

class FundList(ListView):
    allow_empty = True
    model = StudentGreenFund
    paginate_by = 50
    
class FundIndex(ListView):
    queryset = StudentGreenFund.objects.filter(published=True)
            
    def get_context_data(self, **kwargs):
        context = super(FundIndex, self).get_context_data(**kwargs)
        
        context['total_funds'] = StudentGreenFund.objects.filter(published=True).count()
        context['total_campuses'] = StudentGreenFund.objects.filter(published=True).values('institution').distinct().count()
        
        return context

class FundDetail(DetailView):
    queryset = StudentGreenFund.objects.filter(published=True)
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(FundDetail, self).get_context_data(**kwargs)
        return context
        
# CRUD Views
class FundCreateView(CreateView):
    form_class = StudentGreenFund
    template_name = 'greenfunds/create.html'

    def get_form(self, form_class):
        form = form_class(**self.get_form_kwargs())
        form.request = self.request
        return form

    def get_success_url(self):
        return reverse("fund-add-success")

class FundUpdateView(UpdateView):
    model = StudentGreenFund
    form_class = FundUpdateForm
    template_name = 'greenfunds/update.html'

    def get_success_url(self):
        return reverse("fund-edit-success")

    def get_form(self, form_class):
        form = form_class(**self.get_form_kwargs())
        form.request = self.request
        return form

# Overridden search views
class FundSearchView(SearchView):
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