import frappe
import csv

from frappe import get_site_path


def rearrange_fields(**kwargs):
    """Using the file uploaded, update the DocField idx for rearrangement"""
    file_path = get_site_path('public', 'files', kwargs['file'])

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            index = row[0]
            field = row[1]
            frappe.db.sql("""UPDATE `tabDocField` SET idx={0} WHERE fieldname='{1}' AND parent='{2}'""".format(index, field, kwargs['doctype']))
        frappe.db.commit()