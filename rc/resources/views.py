from django.views.generic import ListView

from rc.resources.apps.education.models import CommunityGarden

class ResourceItemListView(ListView):

    def get_context_data(self, **kwargs):
        context = super(ResourceItemListView, self).get_context_data(
            **kwargs)

        context['title'] = self.model._meta.verbose_name_plural.title()
        if 'member_only' in self.kwargs:
            context['member_only'] = self.kwargs['member_only']

        return context

    

