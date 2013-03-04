from django import forms
from rc.resources.apps.greenfunds.models import *
from aashe.organization.models import Organization

# CRUD forms        
class FundCreateForm(forms.ModelForm):
      mandatory = forms.ChoiceField(initial='', choices=COMMITMENT_CHOICES, required=False,
                                             label='Program Commitment',
                                             help_text="Is this fund fee mandatory?")
      term = forms.ChoiceField(initial='', choices=TERM_CHOICES, required=False,
                                             help_text="Please select the term of this fund's fee.")
      
      class Meta:
          model = StudentGreenFund
          fields = ('fund_name', 'institution', 'year',
                    'rate_per_term', 'rate_per_summer_term', 
                    'mandatory', 'term', 'homepage', 'project_contact1_firstname', 
                    'project_contact1_middle', 'project_contact1_lastname', 
                    'project_contact1_confirm', 'project_contact1_title', 
                    'project_contact1_phone', 'project_contact1_department', 
                    'project_contact1_email',)

class FundUpdateForm(forms.ModelForm):
      mandatory = forms.ChoiceField(initial='', choices=COMMITMENT_CHOICES, required=False,
                                             label='Program Commitment',
                                             help_text="Is this fund fee mandatory?")
      term = forms.ChoiceField(initial='', choices=TERM_CHOICES, required=False,
                                             help_text="Please select the term of this fund's fee.")
      
      class Meta:
          model = StudentGreenFund
          fields = ('fund_name', 'institution', 'year',
                    'rate_per_term', 'rate_per_summer_term', 
                    'mandatory', 'term', 'homepage', 'project_contact1_firstname', 
                    'project_contact1_middle', 'project_contact1_lastname', 
                    'project_contact1_confirm', 'project_contact1_title', 
                    'project_contact1_phone', 'project_contact1_department', 
                    'project_contact1_email',)