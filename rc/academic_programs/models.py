from gettext import gettext as _
from django.db import models
from aashe.organization.models import Organization
from csvImporter import fields
from csvImporter.model import CsvModel

# Create your models here.
class AcademicProgram(models.Model):
    title = models.CharField(_('program title'), max_length=256)
    organization = models.ForeignKey(Organization, blank=True, null=True)
    account_num = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True) 
    slug = models.SlugField()
    type = models.CharField(max_length=200, blank=True)
    homepage = models.URLField(max_length=200, blank=True)
    department = models.CharField(max_length=200, blank=True)
    duration = models.TextField(blank=True) 
    founded = models.CharField(max_length=20, blank=True)
    distance_ed = models.TextField(blank=True) 
    commitment = models.TextField(blank=True) 
    language = models.TextField(blank=True) 
    blog = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=255, blank=True)
    discipline = models.CharField(max_length=200, blank=True)
    published = models.BooleanField(_("is published"), blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    
class ProgramCSV(CsvModel):
    title = fields.CharField(match='title')
    # organization = fields.ForeignKey(Organization, pk='account_num', match='organization')
    account_num = fields.IntegerField(match='account_num')
    description = fields.CharField(match='description') 
    type = fields.CharField(match='type') 
    homepage = fields.CharField(match='homepage')
    department = fields.CharField(match='department') 
    duration = fields.CharField(match='duration') 
    founded = fields.CharField(match='founded')
    distance_ed = fields.CharField(match='distance_ed') 
    commitment = fields.CharField(match='commitment') 
    language = fields.CharField(match='language') 
    blog = fields.CharField(match='blog')
    linkedin = fields.CharField(match='linkedin')
    facebook = fields.CharField(match='facebook')
    twitter = fields.CharField(match='twitter')
    discipline = fields.CharField(match='discipline')
    created_date = fields.CharField(match='created_date')
    updated_date = fields.CharField(match='updated_date')
    
    class Meta:
        delimiter = "$"
        silent_failure = False
        has_header = True
        dbModel = AcademicProgram


    