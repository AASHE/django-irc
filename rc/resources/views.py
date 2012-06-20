from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.utils.decorators import classonlymethod
from aashe.aasheauth.decorators import members_only


class ResourceItemListView(ListView):

    def get_context_data(self, **kwargs):
        context = super(ResourceItemListView, self).get_context_data(
            **kwargs)
        opts = self.model._meta

        if not 'title' in context.keys():
            context['title'] = opts.verbose_name_plural.title()

        admin_change_url_name = 'admin:%s_%s_changelist' % (opts.app_label,
                                                            opts.object_name.lower())
        context['admin_changelist_url'] = reverse(admin_change_url_name)

        # So we can pass values from urls.py to templates:
        if self.kwargs:
            context.update(self.kwargs)

        return context
