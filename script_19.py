import frappe


def set_store_details():
    """Setup Pharmakit store settings"""
    settings = frappe.get_doc('Pharmakit Store Settings', 'Pharmakit Store Settings')

    print '[+] Creating INTEREST item'

    # Set interest item
    interest = frappe.get_doc({
        'doctype': 'Item',
        'item_code': 'INTEREST',
        'item_name': 'Interest',
        'is_stock_item': 0,
        'item_group': 'Services'
    }).insert()

    print '[*] Setting up URL and HTTPS'

    # Set URL
    settings.interest = interest.name
    settings.url = 'hub.mypharmakit.com'
    settings.is_https = 1
    settings.save()