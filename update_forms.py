import frappe


def set_fields(**kwargs):
    """
    Set field to hide and be included with columns settings.
    ---
    bench execute xxxx.customize_form.set_fields --kwargs "{'sales': True}"

    """

    d = frappe.get_doc('Customize Form')
    d.doc_type = 'Sales Order Item' if kwargs['sales'] else 'Purchase Order Item'

    # Get the fields
    d.run_method('fetch_to_customize')

    hidden_fields = ['batch_no', 'expiry_date']
    hidden_fields.append('delivery_date' if kwargs['sales'] else 'schedule_date')

    # Hide fields
    for field in hidden_fields:
        try:
            field = d.get('fields', {'fieldname': field})[0]
            field.in_list_view = 0
        except:
            print 'Error in {0}'.format(field)

    fields = {
        'item_code': 1,
        'description': 4,
        'qty': 1,
        'uom': 1,
        'rate': 1,
        'amount': 2
    }

    for field, columns in fields.items():
        field = d.get('fields', {'fieldname': field})[0]

        # Set the list view and columns
        field.in_list_view = 1
        field.columns = columns

    d.run_method('save_customization')
