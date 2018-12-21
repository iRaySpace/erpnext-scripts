import frappe


def set_items(**kwargs):
    items = frappe.get_all('Item', filters={'disabled': 0})
    item_length = len(items)

    for i, item in enumerate(items):
        print 'Setting up {0}/{1} items.'.format(i + 1, item_length)
        frappe.db.sql("""UPDATE `tabItem` SET expense_account=%s WHERE name=%s""", (kwargs['expense_account'], item.name))
        frappe.db.commit()


def set_invoice_items(**kwargs):
    items = frappe.db.sql("""SELECT DISTINCT item_code FROM `tabSales Invoice Item`""", as_dict=True)

    max_items = len(items)

    for i, item in enumerate(items):
        print 'Updating {0}/{1}'.format(i + 1, max_items)
        account = frappe.db.sql("""SELECT expense_account FROM `tabItem` WHERE name=%s""", item.item_code, as_dict=1)[0]
        frappe.db.sql("""UPDATE `tabSales Invoice Item` SET expense_account=%s WHERE item_code=%s""", (account.expense_account, item.item_code))
