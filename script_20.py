import frappe


def set_pharmakit_store_credentials(**kwargs):
    """Set the syncing credentials for the stores"""
    stores = frappe.get_all('Pharmakit Store')

    for store in stores:

        print '[*] Updating {0} credentials'.format(store.name)

        # Update the stores
        store = frappe.get_doc('Pharmakit Store', store.name)
        store.username = kwargs['username']
        store.password = kwargs['password']

        store.save()

    print '[/] Finished processing'