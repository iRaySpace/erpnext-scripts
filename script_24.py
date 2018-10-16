import frappe


def send_email(**kwargs):
    """Create email"""
    email = kwargs['email']
    attachments = [{
        "lang": "en",
        "print_format": "Standard",
        "doctype": "Sales Order",
        "print_letterhead": 1,
        "html": "",
        "print_format_attachment": 1,
        "name": "SO-00222"
    }]
    frappe.sendmail(recipients=[email], subject='Test', message='When you are gone', delayed=False, attachments=attachments)