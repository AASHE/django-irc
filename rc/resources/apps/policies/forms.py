from django import forms
from rc.resources.apps.policies.models import Policy


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
    
