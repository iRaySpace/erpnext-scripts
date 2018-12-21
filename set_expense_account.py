import frappe


def set_items(**kwargs):
    items = frappe.get_all('Item', filters={'disabled': 0})
    item_length = len(items)

    for i, item in enumerate(items):
        print 'Setting up {0}/{1} items.'.format(i + 1, item_length)
        frappe.db.sql("""UPDATE `tabItem` SET expense_account=%s WHERE name=%s""", (kwargs['expense_account'], item.name))
        frappe.db.commit()
