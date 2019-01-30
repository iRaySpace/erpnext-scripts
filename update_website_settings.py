import frappe


def execute(**kwargs):
    website_settings = frappe.get_doc('Website Settings', 'Website Settings')
    website_settings.brand_html = kwargs['brand_html']
    website_settings.save()
