# -*- coding: utf-8 -*-
{
    'name': "bilal_fabrics",

    'summary': """
        This module 'Bilal Fabrics' is about Fabrics shop only for Bilal Sardar's shop""",

    'description': """
        This module 'Bilal Fabrics' is about Fabrics shop only for Bilal Sardar's shop
    """,

    'author': "Farooq Butt",
    'website': "http://www.bilalfabrics.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Fabrics Shop PoS',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'bilal_products', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'reports/bill_reports.xml',
        'views/shop_view.xml',
        'views/menu_view.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
