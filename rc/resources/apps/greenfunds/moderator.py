from django.conf import settings
from aashe.moderation import moderation
from aashe.moderation.moderator import DefaultModerator
from forms import StudentGreenFundCreateForm, StudentGreenFundUpdateForm


class StudentGreenFundModerator(DefaultModerator):
    moderators = getattr(settings, 'MODERATORS', None)
    request_attr = 'request'
moderation.register([StudentGreenFundCreateForm, StudentGreenFundUpdateForm],
                    StudentGreenFundModerator)
