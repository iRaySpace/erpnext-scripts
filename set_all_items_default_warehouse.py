import frappe


def run(**kwargs):
    default_warehouse = kwargs.get('default_warehouse')
    items = frappe.get_all('Item')

    processed = 0

    for item in items:
        item_doc = frappe.get_doc('Item', item['name'])
        item_doc.item_defaults = []
        item_doc.append('item_defaults', {
            'company': frappe.defaults.get_user_default("Company"),
            'default_warehouse': default_warehouse
        })
        item_doc.save()
        processed = processed + 1
        print("Processed {}/{}".format(processed, len(items)))
