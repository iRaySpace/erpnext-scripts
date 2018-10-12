import frappe


def create_customer_stores(**kwargs):
    """Create Customers"""

    print '[+] Adding customer {0}'.format(kwargs['customer'])

    customer = frappe.get_doc({
        'doctype': 'Customer',
        'customer_name': kwargs['customer']
    })

    customer.insert()