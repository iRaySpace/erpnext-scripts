import frappe


def disable_existing_items(**kwargs):
    """Disable existing ERPNext items based on the 'not like' keyword given."""
    items = frappe.get_all('Item', filters={'name': ('not like', '%{0}%'.format(kwargs['keyword']))}, fields=['name'])

    print "---"
    print "Disabling items..."
    print "---"

    # Indices for tracking items to be disabled
    cur_index = 1
    max_index = len(items)

    for item in items:

        # Logging the process
        print "Processing item {0}/{1}.".format(cur_index, max_index)

        item_doc = frappe.get_doc('Item', item.name)
        item_doc.disabled = 1
        item_doc.save()

        cur_index = cur_index + 1

    print "---"
    print "Finished disabling items..."
    print "---"