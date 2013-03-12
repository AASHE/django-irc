from datetime import datetime
from django.http import Http404
from django.db.models import Sum, Count
from django.core.urlresolvers import reverse, reverse_lazy
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
    '''
    Special ListView subclass that auto-populates the template context
    with some useful statistics & summations.
    '''
    def get_context_data(self, **kwargs):
        context = super(FundList, self).get_context_data(**kwargs)
        qs = context['object_list']
        context['total_funds'] = qs.count()
        context['total_campuses'] = qs.values_list(
            'institution__id', flat=True).distinct().count()
        context['states'] = StudentGreenFund.objects.exclude(
            institution__state='').values_list(
            'institution__state', flat=True).distinct().order_by(
            'institution__state')
        return context

class FundMap(FundList):
    template_name = 'greenfunds/studentgreenfund_map.html'
    model = StudentGreenFund  

class FundIndex(FundList):

    def get_context_data(self, **kwargs):
        context = super(FundIndex, self).get_context_data(**kwargs)

        return context

class FundByState(FundList):
    template_name = 'greenfunds/studentgreenfund_state.html'
    model = StudentGreenFund
    
    def get_queryset(self):
        return self.model._default_manager.filter(
            institution__state__iexact=self.kwargs['state'])

    def get_context_data(self, **kwargs):
        context = super(FundByState, self).get_context_data(**kwargs)
        context['state'] = self.kwargs['state']
        return context

class FundByRegion(FundList):
    # regions based on U.S. Census Bureau-designated areas
    NORTHEAST = ('ME', 'NH', 'VT', 'MA', 'RI', 'CT', 'NY', 'PA', 'NJ')
    MIDWEST = ('WI', 'MI', 'IL', 'IN', 'OH', 'MO', 'ND', 'SD', 'NB', 'KS',
               'MN', 'IA')
    SOUTH = ('DE', 'MD', 'DC', 'VA', 'WV', 'NC', 'SC', 'GA', 'FL', 'KY', 'TN',
             'MS', 'AL', 'OK', 'TX', 'AK', 'LA')
    WEST = ('ID', 'MT', 'WY', 'NV', 'UT', 'CO', 'AZ', 'NM', 'AK', 'WA', 'OR',
            'CA', 'HI')
    REGIONS_MAP = {'northeast': {'title': 'Northeastern U.S.', 'states': NORTHEAST},
                   'midwest': {'title': 'Midwestern U.S.', 'states': MIDWEST},
                   'south': {'title': 'Southern U.S.', 'states': SOUTH},
                   'west': {'title': 'Western U.S.', 'states': WEST}}
    
    template_name = 'greenfunds/studentgreenfund_region.html'
    model = StudentGreenFund

    def get_queryset(self):
        state_list = self.REGIONS_MAP.get(self.kwargs['region'])['states']
        return self.model._default_manager.filter(institution__state__in=state_list)

    def get_context_data(self, **kwargs):
        context = super(FundByRegion, self).get_context_data(**kwargs)
        context['region'] = self.REGIONS_MAP.get(self.kwargs['region'])['title']
        context['regions'] = self.REGIONS_MAP.items()
        return context

class FundTypeView(FundList):
    template_name = 'greenfunds/studentgreenfund_control.html'
    model = StudentGreenFund

    def get_queryset(self):
        return self.model._default_manager.filter(institution__is_member=True)

class FundByYear(FundList):
    template_name = 'greenfunds/studentgreenfund_year.html'

    def get_context_data(self, **kwargs):
        context = super(FundByYear, self).get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year', str(datetime.now().year))
        context['years'] = StudentGreenFund.objects.filter(published=True).values_list(
            'year', flat=True).distinct().order_by('-year')
        context['years_extra'] = StudentGreenFund.objects.filter(published=True).values(
            'year').distinct().annotate(Count('id')).order_by("-year")
        return context
    
    def get_queryset(self):
        if 'year' not in self.kwargs:
            return self.model._default_manager.filter(year=str(datetime.now().year))
        else:
            return self.model._default_manager.filter(year=self.kwargs['year'])

class FundByMember(FundList):
    template_name = 'greenfunds/studentgreenfund_member.html'
    model = StudentGreenFund

    def get_queryset(self):
        return self.model._default_manager.filter(institution__is_member=True)

class FundDetail(DetailView):
    queryset = StudentGreenFund.objects.filter(published=True)
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(FundDetail, self).get_context_data(**kwargs)
        return context
        
# CRUD Views
class FundCreateView(CreateView):
    queryset = StudentGreenFund.objects.filter(published=True)
    form_class = StudentGreenFundCreateForm    
    template_name = 'greenfunds/studentgreenfund_create.html'
    success_url = reverse_lazy("green-fund-add-success")

    def get_context_data(self, **kwargs):
        context = super(FundCreateView, self).get_context_data(**kwargs)
        qs = StudentGreenFund.objects.filter(published=True)
     
        return context

class FundUpdateView(UpdateView):
    model = StudentGreenFund
    form_class = StudentGreenFundUpdateForm
    template_name = 'greenfunds/studentgreenfund_update.html'

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