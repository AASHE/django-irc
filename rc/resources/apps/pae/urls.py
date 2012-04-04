from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations
from rc.resources.apps.pae import models


urlpatterns = patterns('',

    url(r'^resources/alumni-sustainability-funds',
        ResourceItemListView.as_view(
            model=models.AlumniFund,
            queryset=handle_missing_organizations(
                models.AlumniFund.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    )

