import frappe


def execute():
    orders = frappe.get_all("Sales Order", fields=['name', 'po_no', 'creation'])
    existing_orders = _group(orders)

    processed = 1
    total_orders = len(orders)

    for order in orders:
        print("Processing {}/{}".format(processed, total_orders))

        po_no = order.get('po_no')
        name = order.get('name')
        existing_order = existing_orders[po_no]

        if name != existing_order.get('name'):
            frappe.delete_doc("Sales Order", name)

        processed = processed + 1


def _group(orders):
    return reduce(_reduce_to_groups, orders, {})


def _reduce_to_groups(_, group):
    po_no = group.get('po_no')

    if po_no in _:
        creation = _compare_creation(_[po_no], group)
        if creation == 1:
            _[po_no] = group
    else:
        _[po_no] = group

    return _


def _compare_creation(a, b):
    a_creation = a.get('creation')
    b_creation = b.get('creation')

    if a_creation > b_creation:
        return 1
    else:
        return -1
