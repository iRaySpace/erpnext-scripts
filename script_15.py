import frappe


def add_sync_user(**kwargs):
    """Creates a sync user to be updated for all of the stores"""

    print '[+] Creating sync user'

    sync_user = frappe.get_doc({
        'doctype': 'User',
        'email': 'sync@sync.com',
        'first_name': 'Sync'
    }).insert()

    print '[*] Updating password'
    sync_user.new_password = kwargs['password']
    sync_user.save()

    # Roles to be added
    roles = ["Accounts Manager", "Accounts User", "Analytics", "Auditor", "Blogger", "Customer", "Employee", "Expense Approver", "Fleet Manager", "Fulfillment User", "Healthcare Administrator", "HR Manager", "HR User", "Item Manager", "Knowledge Base Contributor", "Knowledge Base Editor", "Laboratory User", "LabTest Approver", "Leave Approver", "Maintenance Manager", "Maintenance User", "Manufacturing Manager", "Manufacturing User", "Newsletter Manager", "Nursing User", "Patient", "Pharmakit Manager", "Pharmakit User", "Physician", "Projects Manager", "Projects User", "Purchase Manager", "Purchase Master Manager", "Purchase User", "Quality Manager", "Report Manager", "Rx Physician", "Sales Manager", "Sales Master Manager", "Sales User", "Stock Manager", "Stock User", "Supplier", "Support Team", "System Manager", "Website Manager"]

    for role in roles:
        sync_user.add_roles(role)
        print '[*] Added role {0}'.format(role)

    sync_user.save()

    print 'Finished creation of sync user'
