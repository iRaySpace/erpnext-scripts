import frappe


def set_customer_name_as_name():
    """Gets the customer name and set the document name"""
    customers = frappe.get_all('Customer')

    for customer in customers:
        print '[*] Updating name for the customer {0}'.format(customer.name)

        customer_name = frappe.db.get_value('Customer', customer.name, 'customer_name')
        frappe.db.sql("""UPDATE `tabCustomer` SET name=%s WHERE customer_name=%s""", (customer_name, customer_name))
        frappe.db.commit()

    print '[/] Finished processing'
