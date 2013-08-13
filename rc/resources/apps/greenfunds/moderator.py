from django.conf import settings
from aashe.moderation import moderation
from aashe.moderation.moderator import DefaultModerator
from forms import *


class GreenFundModerator(DefaultModerator):
    moderators = getattr(settings, 'MODERATORS', None)
    request_attr = 'request'

moderation.register(StudentFeeFundCreateForm,
                    GreenFundModerator)

moderation.register(DonationFundCreateForm,
                    GreenFundModerator)

moderation.register(DepartmentFundCreateForm,
                    GreenFundModerator)

moderation.register(HybridFundCreateForm,
                    GreenFundModerator)

moderation.register(GreenFundUpdateForm,
                    GreenFundModerator)