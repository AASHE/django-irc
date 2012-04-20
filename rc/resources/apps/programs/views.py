from rc.resources.apps.policies.models import Policy
from rc.resources.apps.programs.models import Program
from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations


class GreenCleaningProgramAndPolicyListView(ResourceItemListView):

    def __init__(self, *args, **kwargs):
        super(GreenCleaningProgramAndPolicyListView, self).__init__(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GreenCleaningProgramAndPolicyListView,
                        self).get_context_data(**kwargs)

        context['policy_list'] = handle_missing_organizations(
            Policy.objects.filter(type__type='Green Cleaning'))
        context['program_list'] = handle_missing_organizations(
            Program.objects.filter(type__type='Green Cleaning'))

        return context
