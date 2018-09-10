import frappe


def set_item_default_warehouse(**kwargs):
    """Setting items default warehouse"""
    items = frappe.get_all('Item', filters={'disabled': 0, 'name': ('like', '%{0}%'.format(kwargs['keyword']))}, fields=['name'])

    print "---"
    print "Setting as sales item..."
    print "---"

    cur_index = 1
    max_index = len(items)

    for item in items:
        print "Processing item {0}/{1}.".format(cur_index, max_index)

        frappe.db.set_value('Item', item.name, 'default_warehouse', kwargs['warehouse'])

        cur_index = cur_index + 1

    print "---"
    print "Finished setting the default warehouse..."
    print "---"
