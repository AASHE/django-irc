from rc.resources.apps.operations.models import ElectronicWasteEvent
from rc.resources.apps.policies.models import Policy, ElectronicWastePolicy
from rc.resources.apps.programs.models import Program, ElectronicWasteProgram
from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations


class GreenCleaningProgramAndPolicyListView(ResourceItemListView):
    '''Group green cleaning programs and policies.'''

    type = 'Green Cleaning'

    def get_context_data(self, **kwargs):
        context = super(GreenCleaningProgramAndPolicyListView,
                        self).get_context_data(**kwargs)

        context['policy_list'] = handle_missing_organizations(
            Policy.objects.filter(type__type=self.type))
        context['program_list'] = handle_missing_organizations(
            Program.objects.filter(type__type=self.type))

        return context


class ElectronicWasteProgramPolicyAndEventListView(ResourceItemListView):
    '''Group electronic waste programs, policies, and events.'''

    def get_context_data(self, **kwargs):
        context = super(ElectronicWasteProgramPolicyAndEventListView,
                        self).get_context_data(**kwargs)

        context['policy_list'] = handle_missing_organizations(
            ElectronicWastePolicy.objects.all())
        context['program_list'] = handle_missing_organizations(
            ElectronicWasteProgram.objects.all())
        context['event_list'] = handle_missing_organizations(
            ElectronicWasteEvent.objects.all())

        return context
