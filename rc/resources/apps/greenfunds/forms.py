from django import forms
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund  
from aashe.organization.models import Organization

# CRUD forms        
class GreenFundCreateForm(forms.ModelForm):
      
      class Meta:
          model = GreenFund