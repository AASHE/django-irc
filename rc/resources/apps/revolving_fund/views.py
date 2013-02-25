from datetime import datetime
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum, Count
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from haystack.views import SearchView
from aashe.utils.paginator import DiggPaginator as Paginator
from models import RevolvingLoanFund
from forms import RevolvingLoanFundCreateForm, RevolvingLoanFundUpdateForm


class FundListView(ListView):
    '''
    Special ListView subclass that auto-populates the template context
    with some useful statistics & summations.
    '''
    def get_context_data(self, **kwargs):
        context = super(FundListView, self).get_context_data(**kwargs)
        qs = context['object_list']
        context['total_funds'] = qs.count()
        context['total_institutions'] = qs.values_list(
            'institution__id', flat=True).distinct().count()
        context['total_amount'] = qs.aggregate(
            Sum('total_funds'))['total_funds__sum']
        context['billion_participants'] = qs.filter(
            billion_dollar=True).values_list(
            'institution__id').distinct().count()
        context['billion_amount'] = qs.filter(billion_dollar=True).aggregate(
            Sum('total_funds'))['total_funds__sum']
        context['states'] = RevolvingLoanFund.objects.exclude(
            institution__state='').values_list(
            'institution__state', flat=True).distinct().order_by(
            'institution__state')
        return context

class FundDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super(FundDetailView, self).get_context_data(**kwargs)
        qs = RevolvingLoanFund.objects.published()
        context['total_funds'] = qs.count()
        context['total_institutions'] = qs.values_list(
            'institution__id', flat=True).distinct().count()
        context['total_amount'] = qs.aggregate(Sum(
                'total_funds'))['total_funds__sum']
        context['billion_participants'] = qs.filter(
            billion_dollar=True).values_list(
            'institution__id').distinct().count()
        context['billion_amount'] = qs.filter(billion_dollar=True).aggregate(
            Sum('total_funds'))['total_funds__sum']
        context['states'] = RevolvingLoanFund.objects.values_list(
            'institution__state', flat=True).distinct().order_by(
            'institution__state')
        return context    
    
class FundHomepage(FundListView):
    template_name = 'revolving_fund/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(FundHomepage, self).get_context_data(**kwargs)
        context['current_year'] = datetime.now().year
        return context
    
class FundByState(FundListView):
    template_name = 'revolving_fund/revolvingloanfund_state.html'
    model = RevolvingLoanFund
    
    def get_queryset(self):
        return self.model._default_manager.filter(
            institution__state__iexact=self.kwargs['state'])

    def get_context_data(self, **kwargs):
        context = super(FundByState, self).get_context_data(**kwargs)
        context['state'] = self.kwargs['state']
        return context

class FundByYear(FundListView):
    template_name = 'revolving_fund/revolvingloanfund_year.html'

    def get_context_data(self, **kwargs):
        context = super(FundByYear, self).get_context_data(**kwargs)
        context['year'] = self.kwargs['year']
        context['years'] = RevolvingLoanFund.objects.published().values_list(
            'year', flat=True).distinct().order_by('-year')
        return context
    
    def get_queryset(self):
        return self.model._default_manager.filter(year=self.kwargs['year'])
    
class FundByRegion(FundListView):
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
    
    template_name = 'revolving_fund/revolvingloanfund_region.html'
    model = RevolvingLoanFund

    def get_queryset(self):
        state_list = self.REGIONS_MAP.get(self.kwargs['region'])['states']
        return self.model._default_manager.filter(institution__state__in=state_list)

    def get_context_data(self, **kwargs):
        context = super(FundByRegion, self).get_context_data(**kwargs)
        context['region'] = self.REGIONS_MAP.get(self.kwargs['region'])['title']
        context['regions'] = self.REGIONS_MAP.items()
        return context

class FundByMember(FundListView):
    template_name = 'revolving_fund/revolvingloanfund_member.html'
    model = RevolvingLoanFund

    def get_queryset(self):
        return self.model._default_manager.filter(institution__is_member=True)

class FundTypeView(FundListView):
    template_name = 'revolving_fund/revolvingloanfund_control.html'
    model = RevolvingLoanFund

    def get_queryset(self):
        return self.model._default_manager.filter(institution__is_member=True)

class FundTop10(FundListView):
    template_name = 'revolving_fund/revolvingloanfund_top10.html'
    model = RevolvingLoanFund

    def get_context_data(self, **kwargs):
        context = super(FundTop10, self).get_context_data(**kwargs)
        context['largest'] = RevolvingLoanFund.objects.order_by(
            '-total_funds').select_related()[:10]
        context['largest_states'] = RevolvingLoanFund.objects.values(
            'institution__state').distinct().annotate(
            Count('id'), Sum('total_funds')).order_by(
                '-total_funds__sum').select_related()[:10]
        context['most_states'] = RevolvingLoanFund.objects.select_related(
            ).values('institution__state').distinct().annotate(
            Count('id')).order_by('-id__count')[:10]
        context['largest_billion_dollar'] = RevolvingLoanFund.objects.filter(
            billion_dollar=True).order_by('-total_funds').select_related()[:10]
        context['largest_aashe'] = RevolvingLoanFund.objects.filter(
            institution__is_member=True).order_by(
            '-total_funds').select_related()[:10]
        return context

    def get_queryset(self):
        return self.model._default_manager.published()

class FundCarnegieView(FundListView):
    template_name = 'revolving_fund/revolvingloanfund_carnegie.html'
    model = RevolvingLoanFund

    def get_queryset(self):
        carnegie = self.kwargs['carnegie'].lower()
        return self.model._default_manager.filter(
            institution__carnegie_classification__iexact=carnegie)

    def get_context_data(self, **kwargs):
        context = super(FundCarnegieView, self).get_context_data(**kwargs)
        context['carnegie_classes'] = RevolvingLoanFund.objects.values_list(
            "institution__carnegie_classification", flat=True).distinct().order_by(
            "institution__carnegie_classification").exclude(
                institution__carnegie_classification='')
        context['carnegie'] = self.kwargs['carnegie']
        return context

class FundSearchView(SearchView):
    def extra_context(self):
        extra = super(FundSearchView, self).extra_context()
        qs = RevolvingLoanFund.objects.published()
        extra['total_funds'] = qs.count()
        extra['total_institutions'] = qs.values_list(
            'institution__id', flat=True).distinct().count()
        extra['total_amount'] = qs.aggregate(Sum('total_funds'))['total_funds__sum']
        extra['billion_participants'] = qs.filter(
            billion_dollar=True).values_list(
            'institution__id').distinct().count()
        extra['billion_amount'] = qs.filter(billion_dollar=True).aggregate(
            Sum('total_funds'))['total_funds__sum']
        extra['states'] = RevolvingLoanFund.objects.values_list(
            'institution__state', flat=True).distinct().order_by(
            'institution__state')
        return extra

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

class FundUpdateView(UpdateView):
    queryset = RevolvingLoanFund.objects.published()
    form_class = RevolvingLoanFundUpdateForm
    template_name = 'revolving_fund/revolvingloanfund_update.html'
    success_url = reverse_lazy("revolving-fund-update-success")    

    def get_context_data(self, **kwargs):
        context = super(FundUpdateView, self).get_context_data(**kwargs)
        qs = RevolvingLoanFund.objects.published()
        context['total_funds'] = qs.count()
        context['total_institutions'] = qs.values_list(
            'institution__id', flat=True).distinct().count()
        context['total_amount'] = qs.aggregate(
            Sum('total_funds'))['total_funds__sum']
        context['billion_participants'] = qs.filter(
            billion_dollar=True).values_list(
            'institution__id').distinct().count()
        context['billion_amount'] = qs.filter(billion_dollar=True).aggregate(
            Sum('total_funds'))['total_funds__sum']
        context['states'] = RevolvingLoanFund.objects.values_list(
            'institution__state', flat=True).distinct().order_by(
            'institution__state')        
        return context

class FundCreateView(CreateView):
    queryset = RevolvingLoanFund.objects.published()
    form_class = RevolvingLoanFundCreateForm    
    template_name = 'revolving_fund/revolvingloanfund_create.html'
    success_url = reverse_lazy("revolving-fund-create-success")

    def get_context_data(self, **kwargs):
        context = super(FundCreateView, self).get_context_data(**kwargs)
        qs = RevolvingLoanFund.objects.published()
        context['total_funds'] = qs.count()
        context['total_institutions'] = qs.values_list(
            'institution__id', flat=True).distinct().count()
        context['total_amount'] = qs.aggregate(
            Sum('total_funds'))['total_funds__sum']
        context['billion_participants'] = qs.filter(
            billion_dollar=True).values_list(
            'institution__id').distinct().count()
        context['billion_amount'] = qs.filter(billion_dollar=True).aggregate(
            Sum('total_funds'))['total_funds__sum']
        context['states'] = RevolvingLoanFund.objects.values_list(
            'institution__state', flat=True).distinct().order_by(
            'institution__state')        
        return context

class FundStatsMixin(object):
    '''
    Special mixin class that auto-populates the template context
    with some useful statistics & summations.
    '''
    def get_context_data(self, **kwargs):
        context = super(FundStatsMixin, self).get_context_data(**kwargs)
        qs = RevolvingLoanFund.objects.published()
        context['total_funds'] = qs.count()
        context['total_institutions'] = qs.values_list(
            'institution__id', flat=True).distinct().count()
        context['total_amount'] = qs.aggregate(
            Sum('total_funds'))['total_funds__sum']
        context['billion_participants'] = qs.filter(
            billion_dollar=True).values_list(
            'institution__id').distinct().count()
        context['billion_amount'] = qs.filter(billion_dollar=True).aggregate(
            Sum('total_funds'))['total_funds__sum']
        context['states'] = RevolvingLoanFund.objects.values_list(
            'institution__state', flat=True).distinct().order_by(
            'institution__state')        
        return context    
    
# class FundCreate(FundStatsMixin, TemplateView):
#     create_form_class = RevolvingLoanFundCreateForm
#     contact_form_class = FundContactForm
#     success_url = reverse_lazy("revolving-fund-create-success")
#     template_name = 'revolving_fund/revolvingloanfund_create.html'

#     def get_context_data(self, **kwargs):
#         context = FundStatsMixin.get_context_data(self, **kwargs)
#         context.update(kwargs)
#         return context
    
#     def get_form_kwargs(self, prefix=None):
#         kwargs = {}
#         if prefix:
#             kwargs.update({'prefix': prefix})
#         if self.request.method in ('POST', 'PUT'):
#             kwargs.update({
#                     'data': self.request.POST,
#                     'files': self.request.FILES,
#                     })
#         return kwargs

#     def get_forms(self):
#         create = self.create_form_class(**self.get_form_kwargs(prefix='create'))
#         contact = self.contact_form_class(**self.get_form_kwargs(prefix='contact'))
#         return create, contact
    
#     def get(self, request, *args, **kwargs):
#         create_form, contact_form = self.get_forms()
#         return self.render_to_response(self.get_context_data(
#                 create_form=create_form,
#                 contact_form=contact_form))

#     def get_success_url(self):
#         if self.success_url:
#             url = self.success_url % self.fund.__dict__
#         else:
#             try:
#                 url = self.fund.get_absolute_url()
#             except AttributeError:
#                 raise ImproperlyConfigured(
#                     "No URL to redirect to.  Either provide a url or define"
#                     " a get_absolute_url method on the Model.")
#         return url

#     def forms_valid(self, create_form, contact_form):
#         self.fund = create_form.save()
#         self.contact = contact_form.save(commit=False)
#         self.contact.fund = self.fund
#         self.contact.save()
#         return HttpResponseRedirect(self.get_success_url())
    
#     def post(self, request, *args, **kwargs):
#         create_form, contact_form = self.get_forms()
#         if create_form.is_valid() and contact_form.is_valid():
#             return self.forms_valid(create_form, contact_form)
#         else:
#             return self.render_to_response(self.get_context_data(
#                     create_form=create_form,
#                     contact_form=contact_form))
