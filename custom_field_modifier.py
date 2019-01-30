import json
import datetime


def execute(**kwargs):
    """
    Load all of the custom fields, and able to add new fields.
    :param kwargs:
    :return:
    """
    data = []

    with open(kwargs['input']) as json_file:
        data = json.load(json_file)

        display_status(data)

        while get_input():
            data.append(input_custom_field())

    with open(kwargs['output'], 'w') as json_file:
        json_file.write(json.dumps(data, indent=1, sort_keys=True))


def display_status(data):
    custom_fields = [field['fieldname'] for field in data]
    print 'There are {0} custom fields.'.format(len(data))
    print 'The following are the custom fields present: {0}'.format(', '.join(custom_fields))


def get_input():
    choice = raw_input('\nWould you like to add new custom field? (y): ')
    return 1 if choice == 'y' else 0


def input_custom_field():
    required_fields = ['dt', 'fieldname', 'fieldtype', 'insert_after', 'label']

    custom_field = {
        "allow_on_submit": 0,
        "bold": 0,
        "collapsible": 0,
        "collapsible_depends_on": None,
        "columns": 0,
        "default": None,
        "depends_on": None,
        "description": None,
        "docstatus": 0,
        "doctype": "Custom Field",
        "dt": None,
        "fieldname": None,
        "fieldtype": None,
        "hidden": 0,
        "ignore_user_permissions": 0,
        "ignore_xss_filter": 0,
        "in_global_search": 0,
        "in_list_view": 0,
        "in_standard_filter": 0,
        "insert_after": None,
        "label": None,
        "modified": None,
        "name": None,
        "no_copy": 0,
        "options": None,
        "permlevel": 0,
        "precision": "",
        "print_hide": 0,
        "print_hide_if_no_value": 0,
        "print_width": None,
        "read_only": 0,
        "report_hide": 0,
        "reqd": 0,
        "search_index": 0,
        "unique": 0,
        "width": None
    }

    for key, value in custom_field.items():
        if key in required_fields:
            custom_field.update({key: raw_input('Input for {0}: '.format(key)) or "Data"})

    # Update the modified time
    custom_field.update({
        "name": '-'.join([custom_field['dt'], custom_field['fieldname']]),
        "modified": str(datetime.datetime.now())
    })

    return custom_field


execute(input='custom_field_modified.json', output='custom_field_modified2.json')
