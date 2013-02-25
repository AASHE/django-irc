import datetime
from haystack.indexes import *
from haystack import site
from rc.resources.apps.academic_programs.models import AcademicProgram

class AcademicProgramIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    slug = CharField(model_attr='slug')
    description = CharField(model_attr='description', null=True)
    commitment = CharField(model_attr='commitment', null=True)
    program_location = CharField(model_attr='description', null=True)
    # TODO add prepare function that populates this with other_inst field if null
    institution_name = CharField(model_attr='institution__name', null=True)
    other_inst = CharField(model_attr='other_inst', null=True)
    institution_type = CharField(model_attr='institution__org_type', null=True)
    institution_control = CharField(model_attr='institution__sector', null=True)
    institution_stars = BooleanField(model_attr='institution__stars_participant_status', null=True)
    institution_is_member = BooleanField(model_attr='institution__is_member', null=True)
    city = CharField(model_attr='city', null=True)
    state = CharField(model_attr='state', null=True)
    country = CharField(model_attr='country', null=True)
    program_type = CharField(model_attr='program_type__name')
    program_slug = CharField(model_attr='program_type__slug')
    discipline = CharField(model_attr='discipline__name')
    discipline_slug = CharField(model_attr='discipline__slug')
    homepage = CharField(model_attr='homepage')
    distance_ed = CharField(model_attr='distance_ed', null=True)
    
    def index_queryset(self):
      return AcademicProgram.objects.filter(published=True)

site.register(AcademicProgram, AcademicProgramIndex)
