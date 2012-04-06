from base import SimpleTableParser


class ProgramTableParser(SimpleTableParser):

    url = None
    login_required = False

    def processTable(self, table, program_type, headings=True):
        rows = table.findAll('tr')
        if headings:
            rows = rows[1:]
        for row in rows:
            policyData = {}            
            policyData = self.processTableData(row, program_type)
            self.data.append(policyData)

    def processTableData(self, row, program_type):
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
        

