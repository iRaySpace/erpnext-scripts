import frappe


def set_user_role_profile(**kwargs):
    """Set user role profile"""
    user = kwargs['user']
    role_profile = kwargs['role_profile']
    try:
        user = frappe.get_doc('User', user)
        user.role_profile_name = role_profile
        user.save()
        print '[*] User {0} set as {1}'.format(user, role_profile)
    except:
        print '[x] Unable to set role profile {0} to user {1}'.format(role_profile, user)
