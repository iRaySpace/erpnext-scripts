from __future__ import print_function

import frappe


def setup_cost_of_goods_sold(**kwargs):
    """Setup Cost of Goods Sold account"""
    cost_of_goods_sold = frappe.get_doc({
        'doctype': 'Account',
        'parent_account': kwargs['parent'],
        'account_type': 'Cost of Goods Sold',
        'account_name': 'Cost of Goods Sold (GC)'
    })

    cost_of_goods_sold.insert()


def setup_items_expense_account(**kwargs):
    """Setup Items' Expense Account"""
    items = frappe.get_all('Item', filters={'disabled': 0})

    index = 1
    max_len = len(items)

    for item in items:
        print('Processing {0}/{1} Item'.format(index, max_len), end='\r')

        # Set the expense account
        frappe.db.set_value('Item', item.name, 'expense_account', kwargs['expense_account'])

        # Index
        index = index + 1

    print('Processed {0} Items'.format(max_len))
