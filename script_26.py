import frappe


def enable_print_format(**kwargs):
    """Enable specific print format based on the givevn keyword arguments"""
    print_format = kwargs['print_format']

    # Get the Print Format document
    print_format = frappe.get_doc('Print Format', print_format)
    print_format.disabled = 0

    # Save the print format
    print_format.save()
