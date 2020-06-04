{
    'name': 'E3K default forms',
    'version': '0.1',
    'summary': 'E3K_default_forms',
    'category': 'customers_forms',
    'author': 'E3K',
    'depends': ['sale','account'],
    'data': [
        'views/account_invoice_report_views.xml',
        'views/company_form_inherit_views.xml',
        'views/sale_order_inherit_views.xml',
        'views/view_invoice_form_inherit.xml',
    ],
    'sequence': '10',
    'installable': True,
    'auto_install': False,
}
