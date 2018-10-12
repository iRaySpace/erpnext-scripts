import frappe


def set_store_settings(**kwargs):
    """Update the store settings"""
    store_settings = frappe.get_doc('Pharmakit Store Settings', 'Pharmakit Store Settings')

    store_settings.username = kwargs['username']
    store_settings.password = kwargs['password']
    store_settings.save()