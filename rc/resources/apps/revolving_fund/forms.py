from django import forms
from pagedown.widgets import PagedownWidget
from models import RevolvingLoanFund


class RevolvingLoanFundForm(forms.ModelForm):
    description = forms.CharField(widget=PagedownWidget)
    
    class Meta:
        model = RevolvingLoanFund

class RevolvingLoanFundUpdateForm(forms.ModelForm):
    description = forms.CharField(widget=PagedownWidget)
    
    class Meta:
        model = RevolvingLoanFund
        exclude = ('institution', 'slug', 'total_funds_date', 'fund_name',
                   'published', 'pub_date', 'last_updated')

class RevolvingLoanFundCreateForm(forms.ModelForm):
    description = forms.CharField(widget=PagedownWidget)
    
    class Meta:
        model = RevolvingLoanFund
        exclude = ('slug', 'total_funds_date', 'fund_name',
                   'published', 'pub_date', 'last_updated')

        
