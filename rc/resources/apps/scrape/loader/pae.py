from rc.resources.apps.pae.models import AssessmentTool, StudentFeesDescription
from rc.resources.apps.scrape.loader import GenericLoader

class AssessmentToolsLoader(GenericLoader):
    def create_instance(self, data):
        provider_types = dict([(value, key) for key, value in
                               AssessmentTool.CREATORS])
        provider = provider_types.get(data['category'], '')
        data['provider'] = provider
        super(AssessmentToolsLoader, self).create_instance(data)

class StudentFeeLoader(GenericLoader):

    def create_instance(self, data):
        '''The data argument is a dict in this format:

           'institution': name of institution,
           'description': description of student fees for this institution,
           'fees': a list of fees for this institution

        The 'description' element is stashed into a StudentFeesDescription.
        Each of the fees goes into a StudentFee.
        '''
        # Make a StudentFeesDescription:
        student_fees_description = { 'institution': data['institution'],
                                     'description': data['description'],
                                     'organization': None,
                                     'notes': '' }
        super(StudentFeeLoader, self).match_institution(
            student_fees_description)
        obj = StudentFeesDescription(
            organization=student_fees_description['organization'],
            description=student_fees_description['description'],
            notes=student_fees_description['notes'])
        obj.save()
        # Make a number of StudentFees:
        for fee in data['fees']:
            fee['institution'] = data['institution']
            super(StudentFeeLoader, self).create_instance(fee)
