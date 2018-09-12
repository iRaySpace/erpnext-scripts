import frappe


def set_field_included_in_listview(*args, **kwargs):
    """Set field to be included in the listview"""

    # Get the form
    d = frappe.get_doc("Customize Form")
    d.doc_type = kwargs['doc_type']
    d.run_method("fetch_to_customize")
s
    for field in args:
        # Get the field and set to be included in the list view
        d.get("fields", {'fieldname': kwargs['field']})[0].in_list_view = 1

    # Save the form
    d.run_method("save_customization")
