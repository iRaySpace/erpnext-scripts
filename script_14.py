import frappe
import csv

from frappe import get_site_path

def add_item_tax(**kwargs):
    """Check VAT Tax, Update VAT Tax"""
    file_path = get_site_path('public', 'files', kwargs['file'])

    company_name = frappe.defaults.get_global_default('company')
    company = frappe.get_cached_value('Company', company_name, ['abbr'], as_dict=True)

    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file)

        # Counters
        total = 0
        added = 0

        for row in reader:
            sql_query = "SELECT tax_type, tax_rate FROM `tabItem Tax` WHERE parent='{0}' AND tax_type LIKE 'VAT - {1}'".format(
                row['item_code'], company.abbr)

            vat = frappe.db.sql(sql_query, as_dict=1)

            # If VAT already exists
            if vat:

                # Tax Rate
                tax_rate = vat[0].tax_rate

                print '[x] Item "{0}" has {1}% VAT'.format(row['item_code'], tax_rate)

            else:

                # Add the Tax Rate to the Item
                item_doc = frappe.get_doc('Item', row['item_code'])
                item_doc.append('taxes', {
                    'tax_type': 'VAT - {0}'.format(company.abbr),
                    'tax_rate': kwargs['rate']
                })
                item_doc.save()

                print '[+] {0}% VAT has been added to "{1}"'.format(kwargs['rate'], row['item_code'])

                added = added + 1

            total = total + 1

        # Notify
        print 'There are {0}/{1} taxed for 16% VAT - {2}'.format(added, total, frappe.local.site)