from rc.resources.views import ResourceItemListView
import rc.resources.apps.education.models as edmodels


FILTER_RESOURCES_WITH_NO_ORGANIZATION = True

class ResourceItemTablesByOrgCountryView(ResourceItemListView):        

    def get_queryset(self, **kwargs):
        if FILTER_RESOURCES_WITH_NO_ORGANIZATION:
            return self.model.objects.all().filter(
                organization__isnull=False).order_by(
                    'organization__country', 'organization__name')
        else:
            return self.model.objects.all().order_by(
                'organization__country', 'organization__name')

