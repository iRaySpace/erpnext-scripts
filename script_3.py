import frappe


def add_new_item_field(*fields, **keywords):
    """ Create new fields under Item using Custom Field. """

    for field in fields:
        print "Creating {0} custom field...".format(field)
        doc = frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Item",
            "fieldtype": "Data",
            "label": field,
            "insert_after": keywords['insert_after']
        })
        doc.insert()

    print "-----"
    print "Finished creating custom fields..."
    print "-----"
