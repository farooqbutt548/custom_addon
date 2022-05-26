# -*- coding: utf-8 -*-
{
    'name': "bilal_products",

    'summary': """
        this is only used for fetching data of Products""",

    'description': """
        this is only used for fetching data of Products
    """,

    'author': "Farooq Butt",
    'website': "http://www.bilalfabrics.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Repository',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
