from django import forms
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund  
from aashe.organization.models import Organization

# CRUD forms        
class GreenFundCreateForm(forms.ModelForm):
      
      class Meta:
          model = GreenFund

# class StudentFeeFundUpdateForm(forms.ModelForm):
#       mandatory = forms.ChoiceField(initial='', choices=COMMITMENT_CHOICES_EMPTY, required=False,
#                                              label='Program Commitment',
#                                              help_text="Is this fund fee mandatory?")
#       term = forms.ChoiceField(initial='', choices=TERM_CHOICES_EMPTY, required=False,
#                                              help_text="Please select the term of this fund's fee.")
      
#       class Meta:
#           model = StudentFeeFund
#           fields = ('fund_name', 'institution', 'year',
#                     'rate_per_term', 'rate_per_summer_term', 
#                     'mandatory', 'term', 'homepage', 'project_contact1_firstname', 
#                     'project_contact1_middle', 'project_contact1_lastname', 
#                     'project_contact1_confirm', 'project_contact1_title', 
#                     'project_contact1_phone', 'project_contact1_department', 
#                     'project_contact1_email',)

# class DonationFundCreateForm(forms.ModelForm):
#       mandatory = forms.ChoiceField(initial='', choices=COMMITMENT_CHOICES_EMPTY, required=False,
#                                              label='Program Commitment',
#                                              help_text="Is this fund fee mandatory?")
#       term = forms.ChoiceField(initial='', choices=TERM_CHOICES_EMPTY, required=False,
#                                              help_text="Please select the term of this fund's fee.")
      
#       class Meta:
#           model = StudentGreenFund
#           fields = ('fund_name', 'institution', 'year',
#                     'rate_per_term', 'rate_per_summer_term', 
#                     'mandatory', 'term', 'homepage', 'project_contact1_firstname', 
#                     'project_contact1_middle', 'project_contact1_lastname', 
#                     'project_contact1_confirm', 'project_contact1_title', 
#                     'project_contact1_phone', 'project_contact1_department', 
#                     'project_contact1_email',)

# class StudentFeeFundUpdateForm(forms.ModelForm):
#       mandatory = forms.ChoiceField(initial='', choices=COMMITMENT_CHOICES_EMPTY, required=False,
#                                              label='Program Commitment',
#                                              help_text="Is this fund fee mandatory?")
#       term = forms.ChoiceField(initial='', choices=TERM_CHOICES_EMPTY, required=False,
#                                              help_text="Please select the term of this fund's fee.")
      
#       class Meta:
#           model = StudentGreenFund
#           fields = ('fund_name', 'institution', 'year',
#                     'rate_per_term', 'rate_per_summer_term', 
#                     'mandatory', 'term', 'homepage', 'project_contact1_firstname', 
#                     'project_contact1_middle', 'project_contact1_lastname', 
#                     'project_contact1_confirm', 'project_contact1_title', 
#                     'project_contact1_phone', 'project_contact1_department', 
#                     'project_contact1_email',)