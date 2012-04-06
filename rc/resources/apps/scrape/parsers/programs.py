from base import SimpleTableParser


class BicycleSharePrograms(SimpleTableParser):
    '''
    >>> parser = BicycleSharePrograms()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''                                    
    url = 'http://www.aashe.org/resources/bicycle-share-programs'
    login_required = True

    def processTable(self, table, program_type):
        rows = row_tags = table.findAll('tr')
        for row in rows:
            policyData = {}            
            policyData = self.processTableData(row, program_type)
            self.data.append(policyData)

    def processTableData(self, row, program_type):
        els = [ el for el in row ]
        policyData = super(BicycleSharePrograms, 
                           self).processTableData(row, els)
        policyData['program_type'] = program_type
        return policyData

    def parsePage(self):
        tables = self.soup.findAll('table')
        # First 3 tables are 'Free Bicycle Share Programs'
        for table in tables[0:3]:
            self.processTable(table, program_type='Free Bicycle Share Programs')
        # Last table is 'Bicycle Rental Programs'
        self.processTable(tables[-1], program_type='Bicycle Rental Programs')

