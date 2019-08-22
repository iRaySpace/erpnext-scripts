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


def run_two(**kwargs):
    warehouse = kwargs.get('warehouse')
    items = frappe.get_all('Item Default', filters={'default_warehouse': ''}, fields=['name'])

    total_length = len(items)
    processed = 0

    for item in items:
        frappe.db.set_value('Item Default', item['name'], 'default_warehouse', warehouse)
        processed = processed + 1
        print('Processed {}/{}'.format(processed, total_length))

    frappe.db.commit()


def pre_process(**kwargs):
    length = kwargs['length']
    items = frappe.get_all('Item')
    processed = 0

    for item in items:
        if processed == length:
            break

        exists = frappe.db.sql("""
            SELECT 1 FROM `tabItem Default` WHERE parent=%(item)s
        """, {'item': item['name']})

        if exists:
            continue

        item_doc = frappe.get_doc('Item', item['name'])
        item_doc.save()

        processed = processed + 1
        print("Processed {} item(s)".format(processed))
