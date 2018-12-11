from __future__ import print_function

import frappe
import csv


def get_progress_bar(progress):
    """Returns progress bar based on the number"""
    progress_line = "----------".replace('-', '#', progress)
    return '[{:<10s}]'.format(progress_line)


def extract_to_csv():
    """Extract Items to a CSV file"""
    fields = ['name', 'barcode']
    filters = {'disabled': 0}

    # Items
    items = frappe.get_all('Item', filters=filters, fields=fields)

    # File to saved to
    file = open('barcode.csv', 'w')

    # Opening the file
    with file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        # Max length of the items
        max_length = len(items)

        # Write item rows
        for i, item in enumerate(items):

            # Carriage return
            end = '\r'

            # For printing only
            if i + 1 == max_length:
                end = '\n'

            progress = int((float(i+1) / float(max_length)) * 10)
            print('\rWriting {0}/{1} to the csv {2}'.format(i + 1, max_length, get_progress_bar(progress)), end=end)
            writer.writerow(item)


def import_from_csv():
    """Import the barcodes from the csv file"""
    with open('./barcode.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

        # Total items loaded
        max_length = len(rows)

        for i, row in enumerate(rows):

            # Carriage return
            end = '\r'

            # For printing only
            if i + 1 == max_length:
                end = '\n'

            progress = int((float(i + 1) / float(max_length)) * 10)
            print('\rUpdating {0}/{1} to the Item {2}'.format(i + 1, max_length, get_progress_bar(progress)), end=end)
            frappe.db.sql("""UPDATE `tabItem` SET barcode=%s WHERE name=%s""", (row['barcode'], row['name']))

