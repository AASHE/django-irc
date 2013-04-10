from django import forms
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund, HybridFund 
from aashe.organization.models import Organization

# CRUD forms        
class GreenFundCreateForm(forms.ModelForm):
      
      class Meta:
          model = GreenFund

          exclude = ('content_type', 'object_id')

class StudentFeeFundCreateForm(forms.ModelForm):
      
      class Meta:
          model = StudentFeeFund

class DonationFundCreateForm(forms.ModelForm):
      
      class Meta:
          model = DonationFund

class DepartmentFundCreateForm(forms.ModelForm):
      
      class Meta:
          model = DepartmentFund

class HybridFundCreateForm(forms.ModelForm):
      
      class Meta:
          model = HybridFund