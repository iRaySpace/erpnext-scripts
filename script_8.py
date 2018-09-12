import frappe


def set_default_value(*args, **kwargs):
    """Set default value of the field"""

    # Get the form
    d = frappe.get_doc("Customize Form")
    d.doc_type = kwargs['doc_type']
    d.run_method("fetch_to_customize")

    for field in args:
        d.get("fields", {'fieldname': field['field']})[0].default = field['default']

    d.run_method("save_customization")