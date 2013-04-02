from django import forms
from haystack.forms import SearchForm
from haystack.query import SQ, SearchQuerySet
from rc.resources.apps.academic_programs.models import *
from aashe.organization.models import Organization
from aashe.disciplines.models import Discipline

class ProgramsSearchForm(SearchForm):
    # Discipline
    # TODO Add select all options
    discipline = forms.ModelChoiceField(
            queryset = Discipline.objects.all(),
            required = False,
            empty_label = 'Please select',
        )
    # Institution Name picklist
    institution = forms.ModelChoiceField(
            queryset = Organization.objects.filter(sector="Campus"),
            required = False,
        )
    # Degree type (BA, MA, etc.)
    program_type = forms.ModelChoiceField(
            queryset = ProgramType.objects.all(),
            required = False,
            empty_label = 'Please select',
        )
    
    # Institution Type (2-yr (or international equivalent), 4-yr (or international equivalent))
    # TODO reduce this list to choices listed above
    type_choices = []
    type_choices.append((None, 'Please Select'))
    type_values = Organization.objects.filter(sector='campus').exclude(org_type='').order_by('org_type').values("org_type").distinct(),
    # populate choices list
    for value in type_values[0]:
      type_choices.append((value['org_type'], value['org_type']))
    
    institution_type = forms.ChoiceField(
            choices = type_choices,
            required = False,
            widget = forms.Select,
        )
        
    # State/Province (US, Canada only) or by country if outside US, Canada (see member directory for example)
    state_choices = []
    state_choices.append(('', 'Please Select'))
    # state_choices.append(('', 'Please select'))
    state_values = AcademicProgram.objects.exclude(state='').exclude(state=None).order_by('state').values("state").distinct(),
    # populate choices list
    for value in state_values[0]:
      state_choices.append((value['state'], value['state']))
    
    state = forms.ChoiceField(
            choices = state_choices,
            required = False,
            widget = forms.Select,
        )
        
    # Country
    country_choices = []
    country_choices.append(('', 'Please select'))
    country_values = AcademicProgram.objects.exclude(state='').exclude(state=None).order_by('country').values("country").distinct(),
    # populate choices list
    for value in country_values[0]:
      country_choices.append((value['country'], value['country']))

    country = forms.ChoiceField(
            choices = country_choices,
            required = False,
            widget = forms.Select,
        )
        
    # Commitment
    commitment_choices = [('','Please Select')] + list(COMMITMENT_CHOICES)

    commitment = forms.ChoiceField(
            choices = commitment_choices,
            required = False,
            widget=forms.Select,
        )
        
    # Distance Ed
    distance_ed_choices = [('','Please Select')] + list(DISTANCE_CHOICES)

    distance_ed = forms.ChoiceField(
            choices = distance_ed_choices,
            required = False,
            widget=forms.Select,
        )
    
    def search(self):
        # See http://stackoverflow.com/questions/10978695/django-haystack-show-results-without-needing-a-search-query
        # First, store the SearchQuerySet received from other processing.
        sqs = super(ProgramsSearchForm, self).search()

        if not self.is_valid():
          return sqs

        filts = []

        # import pdb
        # pdb.set_trace()

        if self.cleaned_data['discipline']:
          filts.append(SQ(discipline=self.cleaned_data['discipline'].name))
        
        if self.cleaned_data['institution']:
          filts.append(SQ(institution_name=self.cleaned_data['institution'].name))
      
        if self.cleaned_data['program_type']:
          filts.append(SQ(program_type__name=self.cleaned_data['program_type'].name))
          
        if self.cleaned_data['institution_type']:
          filts.append(SQ(institution_type=self.cleaned_data['institution_type']))
        
        if self.cleaned_data['state']:
          filts.append(SQ(state=self.cleaned_data['state']))
        
        if self.cleaned_data['country']:
          filts.append(SQ(country=self.cleaned_data['country']))
        
        if self.cleaned_data['commitment']:
          filts.append(SQ(commitment=self.cleaned_data['commitment']))
        
        if self.cleaned_data['distance_ed']:
          filts.append(SQ(distance_ed=self.cleaned_data['distance_ed']))
          
        if len(filts) > 0 and not self.cleaned_data['q']:
          sqs = SearchQuerySet().load_all()
        
        # Apply the filters
        for filt in filts:
          sqs = sqs.filter(filt)
        
        return sqs

# CRUD forms        
class ProgramCreateForm(forms.ModelForm):
      commitment = forms.ChoiceField(initial='', choices=COMMITMENT_CHOICES, required=False,
                                             label='Program Commitment',
                                             help_text='Is this program full time, part-time, or both?.')
      distance_ed = forms.ChoiceField(initial='', choices=DISTANCE_CHOICES, required=False,
                                             help_text='Is this a distance education program?')
      
      class Meta:
          model = AcademicProgram
          fields = ('title', 'institution', 'other_inst',
                    'description', 'location_name', 'city', 'state', 'country',
                    'program_type', 'homepage', 'department', 'duration', 'founded',
                    'distance_ed', 'commitment', 'language', 'blog', 'facebook', 'linkedin',
                    'twitter', 'discipline', 'project_contact1_firstname', 'project_contact1_middle',
                    'project_contact1_lastname', 'project_contact1_confirm', 'project_contact1_title', 
                    'project_contact1_phone', 'project_contact1_department', 'project_contact1_email',)

class ProgramUpdateForm(forms.ModelForm):
      commitment = forms.ChoiceField(initial='', choices=COMMITMENT_CHOICES, required=False,
                                             label='Program Commitment',
                                             help_text='Is this program full time, part-time, or both?.')
      distance_ed = forms.ChoiceField(initial='', choices=DISTANCE_CHOICES, required=False,
                                             help_text='Is this a distance education program?')
  
      class Meta:
          model = AcademicProgram
          fields = ('title', 'institution', 'other_inst',
                    'description', 'location_name', 'city', 'state', 'country',
                    'program_type', 'homepage', 'department', 'duration', 'founded',
                    'distance_ed', 'commitment', 'language', 'blog', 'facebook', 'linkedin',
                    'twitter', 'discipline', 'project_contact1_firstname', 'project_contact1_middle',
                    'project_contact1_lastname', 'project_contact1_confirm', 'project_contact1_title', 
                    'project_contact1_phone', 'project_contact1_department', 'project_contact1_email',)