import frappe


def set_field_included_in_listview(**kwargs):
    """Set field to be included in the listview"""

    print "================"
    print kwargs['field']
    print kwargs['doc_type']
    print "================"