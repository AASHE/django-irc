from base import PageParser, SimpleTableParser


BASE_URL = 'http://www.aashe.org/resources/'


class ProgramTableParser(SimpleTableParser):

    url = None
    login_required = False

    def processTable(self, table, program_type, headings=True):
        '''
        Same as SimpleTableParser.processTable(), except this passes
        program_type to self.processTableData().
        '''
        rows = table.findAll('tr')
        if headings:
            rows = rows[1:]
        for row in rows:
            policyData = {}
            policyData = self.processTableData(row, program_type)
            self.data.append(policyData)

    def processTableData(self, row, program_type):
        '''
        Tacks program_type on to each proto-Program that's parsed.
        '''
        els = [ el for el in row ]
        policyData = super(ProgramTableParser, self).processTableData(row, els)
        policyData['program_type'] = program_type
        return policyData


class BicycleSharePrograms(ProgramTableParser):
    '''
    >>> parser = BicycleSharePrograms()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'bicycle-share-programs'
    login_required = True

    def parsePage(self):
        tables = self.soup.findAll('table')
        # First 3 tables are 'Free Bicycle Share Programs'
        for table in tables[0:3]:
            super(BicycleSharePrograms, self).processTable(
                table, program_type='Free Bicycle Share Programs')
        # Last table is 'Bicycle Rental Programs'
        super(BicycleSharePrograms, self).processTable(
            tables[-1], program_type='Bicycle Rental Programs')


class CampusCompostingPrograms(ProgramTableParser):
    '''
    >>> parser = CampusComposting()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-composting-programs'
    login_required = True

    def parsePage(self):
        table = self.soup.find('table')
        super(CampusCompostingPrograms, self).processTable(
                table, program_type='Campus Composting Program')


class GreenOfficePrograms(ProgramTableParser):
    '''
    >>> parser = GreenOfficePrograms()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'green-office-programs'
    login_required = True

    def parsePage(self):
        for table in self.soup.findAll('table'):
            super(GreenOfficePrograms, self).processTable(
                table, program_type='Green Office')


class RecyclingWasteMinimization(SimpleTableParser):
    '''
    >>> parser = RecyclingWasteMinimization()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-recycling-and-waste-minimization-websites'
    login_required = True


class StudentSustainabilityEducatorPrograms(PageParser):
    '''
    >>> parser = StudentSustainabilityEducatorPrograms()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'peer-peer-sustainability-outreach-campaigns'
    login_required = True

    def parsePage(self):
        content_div = self.soup.find('div', {'class': 'content clear-block'})
        for paragraph in content_div.findAll('p'):
            resource = {'program_type': 'Student Sustainability Educator'}
            try:
                institution = paragraph.find('strong').extract()
            except AttributeError:
                continue  # *probably* opening text
            resource['institution'] = institution.text
            anchor = paragraph.find('a').extract()
            resource['url'] = anchor['href']
            resource['title'] = anchor.text
            # anything left over is a note
            resource['notes'] = paragraph.text
            self.data.append(resource)


class SurplusPropertyRecyclingPrograms(ProgramTableParser):
    '''
    >>> parser = SurplusPropertyRecycling()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-surplus-recycling'
    login_required = True

    def parsePage(self):
        for table in self.soup.findAll('table'):
            super(SurplusPropertyRecyclingPrograms, self).processTable(
                table, program_type='Surplus Property Recycling')


class GreenCleaningPrograms(ProgramTableParser):
    '''
    >>> parser = GreenCleaningPrograms()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'green-cleaning'
    login_required = True

    def parsePage(self):
        # Programs are listed only in the first table on this page.
        programs_table = self.soup.find('table')
        super(GreenCleaningPrograms, self).processTable(
                table=programs_table, program_type='Green Cleaning')
