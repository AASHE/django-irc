from django.views.generic import ListView

from rc.resources.apps.education.models import CommunityGarden



class ResourceItemListView(ListView):
    '''
    In the context dict passed to as_view(), the following keys are 
    effective:

      - member_only: a boolean, specifies if the view is restricted

      - order_by: a tuple, specifies query set sorting

      - exclude_resources_with_no_organization: a boolean, when True
        resources with no related organization are excluded from the
        query set
    '''

    def get_context_data(self, **kwargs):
        context = super(ResourceItemListView, self).get_context_data(
            **kwargs)

        context['title'] = self.model._meta.verbose_name_plural.title()
        if 'member_only' in self.kwargs:
            context['member_only'] = self.kwargs['member_only']

        return context

    def get_queryset(self, **kwargs):
        qs = self.model.objects.all()
        if 'order_by' in self.kwargs:
            for order in self.kwargs['order_by']:
                qs = qs.order_by(order)
        if 'exclude_resources_with_no_organization' in self.kwargs:
            qs = qs.exclude(organization__isnull=self.kwargs[
                'exclude_resources_with_no_organization'])
        return qs
            
