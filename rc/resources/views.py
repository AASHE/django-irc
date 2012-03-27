from django.views.generic import ListView

from rc.resources.apps.education.models import CommunityGarden

FILTER_RESOURCES_WITH_NO_ORGANIZATION = True


class ResourceItemListView(ListView):

    def get_context_data(self, **kwargs):
        context = super(ResourceItemListView, self).get_context_data(
            **kwargs)

        context['title'] = self.model._meta.verbose_name_plural.title()
        if 'member_only' in self.kwargs:
            context['member_only'] = self.kwargs['member_only']

        return context

    
class ResourceItemTablesByOrgCountryView(ResourceItemListView):        

    def get_queryset(self, **kwargs):
        if FILTER_RESOURCES_WITH_NO_ORGANIZATION:
            return self.model.objects.all().filter(
                organization__isnull=False).order_by(
                    'organization__country', 'organization__name')
        else:
            return self.model.objects.all().order_by(
                'organization__country', 'organization__name')

