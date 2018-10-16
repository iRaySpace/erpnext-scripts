import frappe


def send_email(**kwargs):
    """Create email"""
    email = kwargs['email']
    frappe.sendmail(recipients=[email], subject='Test', message='When you are gone', delayed=False)