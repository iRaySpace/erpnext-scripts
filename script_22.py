import frappe


def add_role_profile(name, restriction):
    """Create a role profile with restrictions"""
    role_profile = frappe.get_doc({
        'doctype': 'Role Profile',
        'role_profile': name
    })

    roles = frappe.get_all('Role')

    for role in roles:

        # Skip any restrictions
        if role.name in restriction:
            continue

        role_profile.append('roles', {
            'role': role.name
        })

        role_profile.save()


def add_full_role_profile():
    """Create a role profile with Full Access"""
    add_role_profile('Pharmakit Full Access', ['Pharmakit User'])


def add_limited_role_profile():
    """Create a role profile with Limited Access"""
    add_role_profile('Pharmakit Limited Access', ['Pharmakit Manager'])


def add_no_role_profile():
    """Create a role profile with No Access"""
    add_role_profile('Pharmakit No Access', ['Pharmakit User', 'Pharmakit Manager'])


def add_role_profiles():
    """Create all of the role profiles"""
    add_full_role_profile()
    add_limited_role_profile()
    add_no_role_profile()