import frappe
import csv


def set_items():
    """
    Using the file, update the Item doctype for their pack sizes.
    Put the file under sites/pack_size.csv
    """

    with open('./pack_size.csv') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        rows = list(reader)
        total_rows = len(rows)

        for i, row in enumerate(rows):
            print 'Updating {0}/{1} ({2}).'.format(i + 1, total_rows, row['item_code'])
            frappe.db.sql("""UPDATE `tabItem` SET pack_size='{0}' WHERE name='{1}'""".format(row['pack_size'], row['item_code']))

        frappe.db.commit()
        print 'Updated a total of {0} items.'.format(total_rows)
