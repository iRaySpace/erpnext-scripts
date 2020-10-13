import frappe


def execute():
    items = frappe.get_all('Item', filters={'show_in_website': 0})
    length = min(1000, len(items))
    print(f'Processing {length} items...')
    for index in range(length):
        item_name = items[index]
        item_doc = frappe.get_doc('Item', item_name)
        item_doc.show_in_website = True
        try:
            item_doc.save()
        except:
            print(f'Failed setting {item_name} show_in_website')
            frappe.log_error(frappe.get_traceback(), 'script: show_in_website failed')
    print('Finished...')
