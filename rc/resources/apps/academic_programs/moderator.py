from django.conf import settings
from aashe.moderation import moderation
from aashe.moderation.moderator import DefaultModerator
from rc.resources.apps.academic_programs.forms import ProgramCreateForm, ProgramUpdateForm

class AcademicProgramModerator(DefaultModerator):
    moderators = getattr(settings, 'MODERATORS', None)
    request_attr = 'request'
moderation.register([ProgramCreateForm, ProgramUpdateForm], AcademicProgramModerator)