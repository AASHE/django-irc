from django import forms
from pagedown.widgets import PagedownWidget
from models import RevolvingLoanFund


class RevolvingLoanFundForm(forms.ModelForm):
    description = forms.CharField(widget=PagedownWidget)
    
    class Meta:
        model = RevolvingLoanFund
