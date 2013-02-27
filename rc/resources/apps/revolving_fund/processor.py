import os
from decimal import Decimal
from django.conf import settings
import xlrd
from models import RevolvingLoanFund
from aashe.organization.models import Organization


FILENAME = os.path.join(settings.SITE_ROOT, '../grfs.xlsx')

book = xlrd.open_workbook(FILENAME)
sh = book.sheet_by_index(0)

names = sh.col_values(0, start_rowx=2)

orgs = []

def process_org(name, state):
    return Organization.objects.get(name=name, state=state)

def process_row(row):
    name, state = row[0], row[3]
    org = process_org(name, state)
    fund_name, year, funds, url = row[5], row[6], str(row[7]), row[8]
    bdc = True if row[4] == 'yes' else False
    funds = Decimal(funds) or 0
    print row[7]
    fund = RevolvingLoanFund.objects.create(
        institution=org,
        billion_dollar=bdc,
        fund_name=fund_name,
        year=str(year),
        total_funds=funds,
        document_url=url)

def process_sheet(sheet):
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        process_row(row)

#process_sheet(sh)
