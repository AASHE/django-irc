from django import forms
from pagedown.widgets import PagedownWidget
from models import RevolvingLoanFund
from aashe.organization.models import Organization


class RevolvingLoanFundUpdateForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=PagedownWidget)
    contact_first_name = forms.CharField(required=True)
    contact_last_name = forms.CharField(required=True)
    contact_email = forms.CharField(required=True)    
    
    class Meta:
        model = RevolvingLoanFund
        exclude = ('institution', 'slug', 'total_funds_date',
                   'published', 'pub_date', 'last_updated')

class RevolvingLoanFundCreateForm(forms.ModelForm):
    institution = forms.ModelChoiceField(
        queryset=Organization.objects.filter(sector='Campus'))
    description = forms.CharField(required=False, widget=PagedownWidget)
    contact_first_name = forms.CharField(required=True)
    contact_last_name = forms.CharField(required=True)
    contact_email = forms.CharField(required=True)
    
    class Meta:
        model = RevolvingLoanFund
        exclude = ('slug', 'total_funds_date', 'published', 'pub_date',
                   'last_updated')
