from django.db.models import Sum
from django.views.generic.list import ListView
from models import RevolvingLoanFund


class FundListView(ListView):
    '''
    Special ListView subclass that auto-populates the template context
    with some useful statistics & summations.
    '''
    def get_context_data(self, **kwargs):
        context = super(FundListView, self).get_context_data(**kwargs)
        qs = context['object_list']
        context['total_funds'] = qs.count()
        context['total_institutions'] = qs.values_list('institution__id', flat=True).distinct().count()
        context['total_amount'] = qs.aggregate(Sum('total_funds'))['total_funds__sum']
        context['billion_participants'] = qs.filter(billion_dollar=True).values_list('institution__id').distinct().count()
        context['billion_amount'] = qs.filter(billion_dollar=True).aggregate(Sum('total_funds'))['total_funds__sum']
        context['states'] = RevolvingLoanFund.objects.values_list('institution__state', flat=True).distinct().order_by('institution__state')        
        return context
    

class FundHomepage(FundListView):
    template_name = 'revolving_fund/homepage.html'
    
class FundByState(FundListView):
    template_name = 'revolving_fund/revolvingloanfund_state.html'
    
    def get_queryset(self):
        return RevolvingLoanFund.objects.filter(institution__state__iexact=self.kwargs['state'])

    def get_context_data(self, **kwargs):
        context = super(FundByState, self).get_context_data(**kwargs)
        context['state'] = self.kwargs['state']
        return context
