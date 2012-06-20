from django.shortcuts import render_to_response
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import RequestContext
from rc.cms.models import Page

class PageView(DetailView):
    queryset = Page.objects.published()
    slug_field = 'path'

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        return context