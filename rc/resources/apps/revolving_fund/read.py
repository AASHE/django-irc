import os
from datetime import date
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
    bdc, fund_name, year, funds, url = row[4], row[5], row[6], row[7], row[8]
    fund = RevolvingLoanFund.objects.create(
        institution=org,
        billion_dollar=bdc,
        fund_name=fund_name,
        year=year,
        total_funds=funds,
        total_funds_date=date.today(),
        document_url=url)

def process_sheet(sheet):
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        process_row(row)

def load_funds():
    process_sheet(sh)
