import frappe


def add_pharmakit_store(**kwargs):
    """Add pharmakit store to the hub"""

    print '[+] Adding {0} for syncing'.format(kwargs['store'])

    store = frappe.get_doc({
        'doctype': 'Pharmakit Store',
        'store_code': kwargs['store'],
        'url': kwargs['url'],
        'is_https': 1,
        'username': kwargs['username'],
        'password': kwargs['password']
    }).insert()
