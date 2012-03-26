from rc.resources.views import ResourceItemListView
import rc.resources.apps.education.models as edmodels


FILTER_GARDENS_WITH_NO_ORGANIZATION = True

class CommunityGardenListView(ResourceItemListView):

    context_object_name = 'communitygardens'
    model = edmodels.CommunityGarden

    def get_context_data(self, **kwargs):
        context = super(CommunityGardenListView, self).get_context_data(
            **kwargs)

        context['member_only'] = True

        context['opening_text'] = """
        This resource lists campus and campus-community gardens that
        use organic gardening techniques and have a student learning
        component. Additionally, refer to <a
        href="http://www.bamco.com/uploads/documents/student_garden_guide_final_-_food_service.pdf">Bon
        Appetit's Student Gardens Guide</a> and <a
        href="http://www.youtube.com/watch?v=2eAYgF57Vrw">related
        video</a> for information and guidance on establishing a
        garden on your campus."""

        context['guts'] = 'education/communitygarden_list_guts.html'
    
        context['closing_text'] = """
        <em>Please email <a href="mailto:resources@aashe.org">
        resources@aashe.org</a> with any suggestions, additions or 
        updates.</em>"""

        return context

    def get_queryset(self, **kwargs):
        if FILTER_GARDENS_WITH_NO_ORGANIZATION:
            return self.model.objects.all().filter(
                organization__isnull=False).order_by(
                    'organization__country', 'organization__name')
        else:
            return self.model.objects.all().order_by(
                'organization__country', 'organization__name')

        
class CampusAgricultureListView(ResourceItemListView):

    model = edmodels.CampusAgriculture
    
    def get_context_data(self, **kwargs):
        context = super(CampusAgricultureListView, self).get_context_data(
            **kwargs)

        context['member_only'] = True

        context['opening_text'] = """
            This resource is a collection of campus farms and
            campus supported agriculture programs that are sources of
            sustainable food for the campus community. While produce
            from campus community gardens is usually reserved for use
            by plot-owners, CSA farms and programs supply locally
            grown food to campus eateries and members of the campus
            community."""

        context['guts'] = 'education/campusagriculture_list_guts.html'
    
        context['closing_text'] = """
            <em>Please email <a href="mailto:resources@aashe.org">
            resources@aashe.org</a> with any suggestions, additions or 
            updates.</em>"""

        return context
        
