import frappe


def disable_existing_items(**kwargs):
    """Disable existing ERPNext items based on the 'not like' keyword given."""
    items = frappe.get_all('Item', filters={'name': ('not like', '%{0}%'.format(kwargs['keyword']))}, fields=['name'])

    print "Disabling items..."

    for item in items:
        item_doc = frappe.get_doc('Item', item.name)
        item_doc.disabled = 1
        item_doc.save()

    print "Finished disabling items..."
