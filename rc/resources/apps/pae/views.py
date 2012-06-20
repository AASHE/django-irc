from rc.resources.views import ResourceItemListView
from rc.resources.apps.pae.models import StudentFeesDescription, StudentFee

class StudentFeeListView(ResourceItemListView):

    def get_context_data(self, **kwargs):
        '''StudentFees are displayed by institution, and preceeded by
        some text that's stored in a StudentFeesDescription record.
        The 'matched_descriptions' and 'unmatched_fees' elements added
        to context_data can be used in a template, rather than object_list.
        '''
        context = super(StudentFeeListView, self).get_context_data(**kwargs)

        matched_descriptions = list()
        for descr in StudentFeesDescription.objects.exclude(
                organization__isnull=True).order_by('organization__name'):
            fees = StudentFee.objects.filter(
                organization=descr.organization).order_by('title')
            matched_descriptions.append({ 'description': descr.description,
                                          'organization': descr.organization,
                                          'fees': fees })
        context['matched_descriptions'] = matched_descriptions

        context['unmatched_fees'] = StudentFee.objects.filter(
            organization__isnull=True).order_by('title')

        return context
