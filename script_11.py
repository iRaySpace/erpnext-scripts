import frappe


def set_all_item_field_value(**kwargs):
    """Set all items based on the value given and filters"""

    # Filters
    filters = {
        'disabled': 0,
        'is_purchase_item': 0,
        'name': ('like', '%{0}%'.format(kwargs['keyword']))
    }

    # Get all Item fields based from the filters
    items = frappe.get_all('Item', filters=filters, fields=['name'])

    # Counters
    cur_index = 1
    max_index = len(items)

    print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
    print "Setting all Item {0} field to the value {1}.".format(kwargs['field'], kwargs['value'])
    print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="

    for item in items:
        print "Processing item {0}/{1}...".format(cur_index, max_index)

        frappe.db.set_value('Item', item.name, kwargs['field'], kwargs['value'])

        cur_index = cur_index + 1

    print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
    print "Done setting {1} items.".format(max_index)
    print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
