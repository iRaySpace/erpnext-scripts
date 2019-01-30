import frappe

from frappe.installer import install_app as _install_app


def execute(**kwargs):
    """
    Use this to install apps; it checks for apps that are already installed.
    bench --site [site_name] execute [module_name].install_apps.execute
        --kwargs "{'apps': ['rebrandly_integration', 'printnode_integration']}"
    """
    apps_installed = frappe.db.sql("""SELECT DISTINCT app_name FROM `tabModule Def`""", as_dict=True)
    apps_installed = [v.app_name for v in apps_installed]

    for app in kwargs['apps']:
        if app not in apps_installed:
            print 'Installing app {0}'.format(app)

            frappe.init(site=kwargs['site'])
            frappe.connect()

            try:
                _install_app(app, verbose=False)
            finally:
                frappe.destroy()


