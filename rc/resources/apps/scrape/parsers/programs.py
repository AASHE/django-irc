from base import SimpleTableParser


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
    url = 'http://www.aashe.org/resources/bicycle-share-programs'
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
    url = 'http://www.aashe.org/resources/campus-composting-programs'
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
    url = 'http://www.aashe.org/resources/green-office-programs'
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
    url = 'http://www.aashe.org/resources/campus-recycling-and-waste-minimization-websites'
    login_required = True


class SurplusPropertyRecyclingPrograms(ProgramTableParser):
    '''
    >>> parser = SurplusPropertyRecycling()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-surplus-recycling'
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
    url = 'http://www.aashe.org/resources/green-cleaning'
    login_required = True

    def parsePage(self):
        # Programs are listed only in the first table on this page.
        programs_table = self.soup.find('table')
        super(GreenCleaningPrograms, self).processTable(
                table=programs_table, program_type='Green Cleaning')
