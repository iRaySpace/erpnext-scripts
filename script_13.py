import frappe
import csv

from frappe import get_site_path

def update_item_price(**kwargs):
    """Updates the Purchase Order Price"""
    file_path = get_site_path('public', 'files', kwargs['file'])
    
    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print 'Processing {0}.'.format(row['item_code'])

            item_price_query = frappe.db.sql("""SELECT name FROM `tabItem Price` WHERE item_code=%s AND price_list='Standard Buying'""", row['item_code'], as_dict=1)

            # If the Item Price is already exist
            if item_price_query:
                item_price = frappe.get_doc('Item Price', item_price_query[0].name)
                item_price.price_list_rate = row['new_price']
                item_price.save()
            else:
                print 'Item Price for {0} does not exist. Creating one.'.format(row['item_code'])
                item_price = frappe.get_doc({
                    'doctype': 'Item Price',
                    'item_code': row['item_code'],
                    'price_list': 'Standard Buying',
                    'price_list_rate': row['new_price']
                })
                item_price.insert()

        print 'Finished processing...'
