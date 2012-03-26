from django.views.generic import ListView


class ResourceItemListView(ListView):

    # model must be overridden by subclass
    model = None
    template_name = 'resourceitem_list.html'

    def get_context_data(self, **kwargs):
        context = super(ResourceItemListView, self).get_context_data(
            **kwargs)

        context['title'] = self.model._meta.verbose_name_plural.title()

        return context

    

