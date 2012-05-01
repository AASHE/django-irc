from django.views.generic import ListView


class ResourceItemListView(ListView):

    def get_context_data(self, **kwargs):
        context = super(ResourceItemListView, self).get_context_data(
            **kwargs)

        if not 'title' in context.keys():
            context['title'] = self.model._meta.verbose_name_plural.title()

        # So we can pass values from urls.py to templates:
        if self.kwargs:
            context.update(self.kwargs)

        return context
