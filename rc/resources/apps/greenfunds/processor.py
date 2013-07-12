import os
from decimal import Decimal
from django.conf import settings
import xlrd
from models import *
from aashe.organization.models import Organization

# usage: from rc.resources.apps.greenfunds.processor import *

FILENAME = os.path.join(settings.SITE_ROOT, '../rc/resources/apps/greenfunds/greenfunds.xlsx')

book = xlrd.open_workbook(FILENAME)
donation_sheet = book.sheet_by_index(0)
donation_names = donation_sheet.col_values(0, start_rowx=2)

fee_sheet = book.sheet_by_index(1)
fee_names = fee_sheet.col_values(0, start_rowx=2)

orgs = []

def process_org(name, state=None):
    try:
        if state:
            org = Organization.objects.get(picklist_name=name, state=state)
        else:
            org = Organization.objects.get(picklist_name=name)
        return org
    except Organization.DoesNotExist:
        print "%s not a valid org" % name


def process_term(name):
    term_choices = dict([(value, key) for key, value in TERM_CHOICES])
    term_type = term_choices.get(name, '')
    return term_type

def process_donation_row(row):
    donation_source_description = row[1]
    name = row[3]
    org = process_org(name)
    fund_name = row[2]
    if fund_name == "":
        fund_name = "Unknown/Other"
    year = row[4]
    # needed to avoid invalid literal error
    if year == '':
        year = None
    homepage = row[5]
    fund_size = row[6]
    if fund_size == '':
        fund_size = None
    fund_description = row[7]
    # omit recipients
    project_contact1_firstname = row[9]
    project_contact1_middle = row[10]
    project_contact1_lastname = row[11]
    project_contact1_email = row[12]
    project_contact1_title = row[13]
    project_contact1_phone = row[14]
    project_contact1_department = row[15]
    notes = row[16]
    # TODO put comment fields for all rows in notes
    fund = DonationFund.objects.create(
        donation_source_description=donation_source_description,
        institution=org,
        fund_name=fund_name,
        fund_description=fund_description,
        year=year,
        fund_size=fund_size,
        homepage=homepage,
        published=True,
        project_contact1_firstname=project_contact1_firstname,
        project_contact1_middle=project_contact1_middle,
        project_contact1_lastname=project_contact1_lastname,
        project_contact1_email=project_contact1_email,
        project_contact1_title=project_contact1_title,
        project_contact1_phone=project_contact1_phone,
        project_contact1_department=project_contact1_department,
        notes=notes)

def process_fee_row(row):
    name = row[2]
    org = process_org(name)
    fund_name = row[1]
    if fund_name == "":
        fund_name = "Unknown/Other"
    year = row[3]
    homepage = row[4]
    rate_per_term = row[5]
    term = process_term(row[6])
    fund_description = row[7]
    # omit recipients
    project_contact1_firstname = row[9]
    project_contact1_middle = row[10]
    project_contact1_lastname = row[11]
    project_contact1_email = row[12]
    project_contact1_title = row[13]
    project_contact1_phone = row[14]
    project_contact1_department = row[15]
    notes = row[16]
    # TODO put comment fields for all rows in notes
    fund = StudentFeeFund.objects.create(
        institution=org,
        fund_name=fund_name,
        fund_description=fund_description,
        year=year,
        rate_per_term=rate_per_term,
        term=term,
        homepage=homepage,
        published=True,
        project_contact1_firstname=project_contact1_firstname,
        project_contact1_middle=project_contact1_middle,
        project_contact1_lastname=project_contact1_lastname,
        project_contact1_email=project_contact1_email,
        project_contact1_title=project_contact1_title,
        project_contact1_phone=project_contact1_phone,
        project_contact1_department=project_contact1_department,
        notes=notes)

def process_fee_sheet(sheet):
    StudentFeeFund.objects.all().delete()
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        process_fee_row(row)

def process_donation_sheet(sheet):
    DonationFund.objects.all().delete()
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        process_donation_row(row)

#process_sheet(sh)
