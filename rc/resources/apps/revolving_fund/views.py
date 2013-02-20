from datetime import datetime
from django.db.models import Sum, Count
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from haystack.views import SearchView
from aashe.utils.paginator import DiggPaginator as Paginator
from models import RevolvingLoanFund
from forms import RevolvingLoanFundForm


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
        context['states'] = RevolvingLoanFund.objects.values_list(
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
            page_no = int(self.requrest.GET.get('page', 1))
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
    form_class = RevolvingLoanFundForm
    template_name = 'revolving_fund/revolvingloanfund_update.html'

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
    form_class = RevolvingLoanFundForm    
    template_name = 'revolving_fund/revolvingloanfund_create.html'

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
    
