import frappe


def set_field_columns(*args, **kwargs):
    """Set the field columns"""

    d = frappe.get_doc("Customize Form")
    d.doc_type = kwargs['doc_type']
    d.run_method("fetch_to_customize")

    for field in args:
        d.get("fields", {'fieldname': field['field']})[0].columns = field['columns']

    d.run_method("save_customization")