import frappe


def edit_item_fieldtype(*fields, **keywords):
    """ Change fields' fieldtype"""

    for field in fields:
        print "Modifying {0} field type...".format(field)
        doc = frappe.get_doc("Custom Field", keywords['doctype'] + "-" + field)
        doc.fieldtype = keywords['fieldtype']
        doc.save()

    print "-----"
    print "Finished modifying field types..."
    print "-----"