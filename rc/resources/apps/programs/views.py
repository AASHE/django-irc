from rc.resources.apps.policies.models import Policy
from rc.resources.apps.programs.models import Program
from rc.resources.models import ResourceArea
from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations


def get_query_set_for_model_for_resource_area(model, resource_area,
                                              order_by=None):
    qs = model.objects.filter(resource_areas=resource_area)
    if order_by:
        qs = qs.order_by(*order_by)
    qs = handle_missing_organizations(qs)
    return qs


class GreenCleaningProgramAndPolicyListView(ResourceItemListView):

    resource_area_name = 'Green Cleaning Programs & Policies'

    def __init__(self, *args, **kwargs):
        super(GreenCleaningProgramAndPolicyListView, self).__init__(
            *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GreenCleaningProgramAndPolicyListView,
                        self).get_context_data(**kwargs)

        context['policy_list'] = self._get_query_set(Policy)
        context['program_list'] = self._get_query_set(Program)

        return context

    def _get_query_set(self, model):
        resource_area = ResourceArea.objects.get(area=self.resource_area_name)

        qs = get_query_set_for_model_for_resource_area(
            model=model, resource_area=resource_area,
            order_by=('organization__country', 'organization__name'))
        return qs
