import frappe
import csv


def load_db():
    with open('./medical_codes.csv') as file:
        data = csv.DictReader(file)
        rows = list(data)

        max_length = len(rows)

        duplicates = []

        for i, row in enumerate(rows):
            print 'Loading {0}/{1} Medical Code.'.format(i + 1, max_length)
            medical_code = frappe.get_doc({
                'doctype': 'Medical Code',
                'medical_code_standard': 'ICD-10',
                'code': row['medical_code'],
                'description': row['description']
            })

            try:
                medical_code.save()
            except:
                duplicates.append(row)

        print 'The following are the duplicates:'
        print duplicates


def clear_db():
    frappe.db.sql("""DELETE FROM `tabMedical Code`""")
