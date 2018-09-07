import frappe


def hide_doc_fields(*fields, **kwargs):
    """This method hides field using Customize Form"""
    c_frm = frappe.get_doc("Customize Form")
    c_frm.doc_type = kwargs['doc_type']
    c_frm.run_method("fetch_to_customize")

    for field in fields:
        c_frm.get("fields", {"fieldname": field})[0].hidden = 1

    c_frm.run_method("save_customization")