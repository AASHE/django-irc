from itertools import chain
from datetime import datetime
from django.http import Http404
from django.db.models import Sum, Count
from django.core.urlresolvers import reverse, reverse_lazy, resolve
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from aashe.disciplines.models import Discipline
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.edit import CreateView, UpdateView, FormView
from haystack.views import SearchView, search_view_factory
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund, HybridFund
from forms import *
from django.core.paginator import InvalidPage, EmptyPage #, Paginator
from rc.resources.apps.academic_programs.digg_paginator import DiggPaginator as Paginator


class FundList(ListView):
    '''
    Special ListView subclass that auto-populates the template context
    with some useful statistics & summations.
    '''
    # model = GreenFund
    queryset=list(chain(StudentFeeFund.objects.filter(published=True),
          DonationFund.objects.filter(published=True),
          DepartmentFund.objects.filter(published=True),
          HybridFund.objects.filter(published=True),)),

    def get_context_data(self, **kwargs):
        context = super(FundList, self).get_context_data(**kwargs)
        qs = context['object_list']
        context['total_funds'] = GreenFund.objects.filter(published=True).count()
        context['total_campuses'] = GreenFund.objects.filter(published=True).values_list(
            'institution__id', flat=True).distinct().count()
        context['states'] = GreenFund.objects.filter(published=True).exclude(
            institution__state='').values_list(
            'institution__state', flat=True).distinct().order_by(
            'institution__state')
        return context

class FundMap(FundList):
    template_name = 'greenfunds/greenfund_map.html'

class FundIndex(FundList):
    def get_context_data(self, **kwargs):
        context = super(FundIndex, self).get_context_data(**kwargs)

        return context

class FundByState(FundList):
    template_name = 'greenfunds/greenfund_state.html'

    def get_queryset(self):
        return list(chain(StudentFeeFund.objects.filter(published=True, institution__state__iexact=self.kwargs['state']),
          DonationFund.objects.filter(published=True, institution__state__iexact=self.kwargs['state']),
          DepartmentFund.objects.filter(published=True, institution__state__iexact=self.kwargs['state']),
          HybridFund.objects.filter(published=True, institution__state__iexact=self.kwargs['state']),))

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

    template_name = 'greenfunds/greenfund_region.html'

    def get_queryset(self):
        state_list = self.REGIONS_MAP.get(self.kwargs['region'])['states']
        return list(chain(StudentFeeFund.objects.filter(published=True, institution__state__in=state_list),
          DonationFund.objects.filter(published=True, institution__state__in=state_list),
          DepartmentFund.objects.filter(published=True, institution__state__in=state_list),
          HybridFund.objects.filter(published=True, institution__state__in=state_list),))

    def get_context_data(self, **kwargs):
        context = super(FundByRegion, self).get_context_data(**kwargs)
        context['region'] = self.REGIONS_MAP.get(self.kwargs['region'])['title']
        context['regions'] = self.REGIONS_MAP.items()
        return context

class FundTypeView(FundList):
    template_name = 'greenfunds/greenfund_control.html'

    def get_queryset(self):
        return list(chain(StudentFeeFund.objects.filter(published=True, institution__is_member=True),
          DonationFund.objects.filter(published=True, institution__is_member=True),
          DepartmentFund.objects.filter(published=True, institution__is_member=True),
          HybridFund.objects.filter(published=True, institution__is_member=True),))

class FundByYear(FundList):
    template_name = 'greenfunds/greenfund_year.html'

    def get_context_data(self, **kwargs):
        context = super(FundByYear, self).get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year', str(datetime.now().year))
        context['years'] = GreenFund.objects.filter(published=True).values_list(
            'year', flat=True).distinct().order_by('-year')
        context['years_extra'] = GreenFund.objects.filter(published=True).values(
            'year').distinct().annotate(Count('id')).order_by("-year")
        return context

    def get_queryset(self):
        if 'year' not in self.kwargs:
            return list(chain(StudentFeeFund.objects.filter(published=True, year=str(datetime.now().year)),
                  DonationFund.objects.filter(published=True, year=str(datetime.now().year)),
                  DepartmentFund.objects.filter(published=True, year=str(datetime.now().year)),
                  HybridFund.objects.filter(published=True, year=str(datetime.now().year)),))
        else:
            return list(chain(StudentFeeFund.objects.filter(published=True, year=self.kwargs['year']),
                  DonationFund.objects.filter(published=True, year=self.kwargs['year']),
                  DepartmentFund.objects.filter(published=True, year=self.kwargs['year']),
                  HybridFund.objects.filter(published=True, year=self.kwargs['year']),))

class FundByMember(FundList):
    template_name = 'greenfunds/greenfund_member.html'
    model = GreenFund

    def get_queryset(self):
        return list(chain(StudentFeeFund.objects.filter(published=True, institution__is_member=True),
                  DonationFund.objects.filter(published=True, institution__is_member=True),
                  DepartmentFund.objects.filter(published=True, institution__is_member=True),
                  HybridFund.objects.filter(published=True, institution__is_member=True),))

class FundCarnegieView(FundList):
    template_name = 'greenfunds/greenfund_carnegie.html'
    queryset=list(chain(StudentFeeFund.objects.filter(published=True),
          DonationFund.objects.filter(published=True),
          DepartmentFund.objects.filter(published=True),
          HybridFund.objects.filter(published=True),)),

    def get_queryset(self):
        carnegie = self.kwargs['carnegie'].lower()
        return list(chain(StudentFeeFund.objects.filter(published=True, institution__carnegie_classification__iexact=carnegie),
                  DonationFund.objects.filter(published=True, institution__carnegie_classification__iexact=carnegie),
                  DepartmentFund.objects.filter(published=True, institution__carnegie_classification__iexact=carnegie),
                  HybridFund.objects.filter(published=True, institution__carnegie_classification__iexact=carnegie),))

    def get_context_data(self, **kwargs):
        context = super(FundCarnegieView, self).get_context_data(**kwargs)
        context['carnegie_classes'] = GreenFund.objects.values_list(
            "institution__carnegie_classification", flat=True).distinct().order_by(
            "institution__carnegie_classification").exclude(
                institution__carnegie_classification='')
        context['carnegie'] = self.kwargs['carnegie']
        return context

class HybridFundDetail(DetailView):
    queryset = HybridFund.objects.filter(published=True)
    model = HybridFund
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(HybridFundDetail, self).get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context

class DepartmentFundDetail(DetailView):
    queryset = DepartmentFund.objects.filter(published=True)
    model = DepartmentFund
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(DepartmentFundDetail, self).get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context

class StudentFeeFundDetail(DetailView):
    queryset = StudentFeeFund.objects.filter(published=True)
    model = StudentFeeFund
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(StudentFeeFundDetail, self).get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context

class DonationFundDetail(DetailView):
    queryset = DonationFund.objects.filter(published=True)
    model = DonationFund
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(DonationFundDetail, self).get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context

# CRUD Views
class FundCreateView(CreateView):
    template_name = 'greenfunds/greenfund_create.html'
    success_url = reverse_lazy("green-fund-add-success")

    def get_context_data(self, **kwargs):
        context = super(FundCreateView, self).get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        return context

class StudentFeeFundUpdateView(UpdateView):
    queryset = StudentFeeFund.objects.all()
    model = StudentFeeFund
    # form_class = GreenFundUpdateForm
    template_name = 'greenfunds/greenfund_update.html'
    success_url = reverse_lazy("green-fund-edit-success")

    def get_form(self, form_class):
        form = form_class(**self.get_form_kwargs())
        form.request = self.request
        return form

    def get_context_data(self, **kwargs):
        context = super(StudentFeeFundUpdateView, self).get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        return context

class DonationFundUpdateView(UpdateView):
    queryset = DonationFund.objects.all()
    model = DonationFund
    # form_class = GreenFundUpdateForm
    template_name = 'greenfunds/greenfund_update.html'
    success_url = reverse_lazy("green-fund-edit-success")

    def get_form(self, form_class):
        form = form_class(**self.get_form_kwargs())
        form.request = self.request
        return form

    def get_context_data(self, **kwargs):
        context = super(DonationFundUpdateView, self).get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        return context

class DepartmentFundUpdateView(UpdateView):
    queryset = DepartmentFund.objects.all()
    model = DepartmentFund
    # form_class = GreenFundUpdateForm
    template_name = 'greenfunds/greenfund_update.html'
    success_url = reverse_lazy("green-fund-edit-success")

    def get_form(self, form_class):
        form = form_class(**self.get_form_kwargs())
        form.request = self.request
        return form

    def get_context_data(self, **kwargs):
        context = super(DepartmentFundUpdateView, self).get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        return context

class HybridFundUpdateView(UpdateView):
    queryset = HybridFund.objects.all()
    model = HybridFund
    # form_class = GreenFundUpdateForm
    template_name = 'greenfunds/greenfund_update.html'
    success_url = reverse_lazy("green-fund-edit-success")

    def get_form(self, form_class):
        form = form_class(**self.get_form_kwargs())
        form.request = self.request
        return form

    def get_context_data(self, **kwargs):
        context = super(HybridFundUpdateView, self).get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        return context

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