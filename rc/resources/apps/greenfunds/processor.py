import os
from decimal import Decimal
from django.conf import settings
import xlrd
from models import *
from aashe.organization.models import Organization


FILENAME = os.path.join(settings.SITE_ROOT, '../rc/resources/apps/greenfunds/greenfunds.xlsx')

book = xlrd.open_workbook(FILENAME)
sh = book.sheet_by_index(0)

names = sh.col_values(0, start_rowx=2)

orgs = []

def process_org(name, state):
    org = Organization.objects.get(name=name, state=state)
    return org

def process_term(name):
    term_choices = dict([(value, key) for key, value in TERM_CHOICES])
    term_type = term_choices.get(name, '')
    return term_type

def process_row(row):
    name, state = row[0], row[3]
    org = process_org(name, state)
    fund_name = row[5]
    if fund_name == "":
        fund_name = "Unknown/Other"
    year = row[6]
    rate_per_term = row[7]
    # rate_per_summer_term = row[9]
    term = process_term(row[8])
    homepage = row[11]
    # TODO put comment fields for all rows in notes
    fund = StudentFeeFund.objects.create(
        institution=org,
        fund_name=fund_name,
        year=year,
        rate_per_term=rate_per_term,
        term=term,
        homepage=homepage,
        published=True)

def process_sheet(sheet):
    StudentFeeFund.objects.all().delete()
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        process_row(row)

#process_sheet(sh)
