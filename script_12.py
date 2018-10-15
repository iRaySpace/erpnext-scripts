import frappe


def set_pos_mode(**kwargs):
    """Set the POS mode as Offline(1) or Online(0)"""
    settings = frappe.get_doc('POS Settings', 'POS Settings')
    settings.use_pos_in_offline_mode = kwargs['mode']
    settings.save()
