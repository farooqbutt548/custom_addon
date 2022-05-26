# -*- coding: utf-8 -*-
{
    # 'name': "fabrics",
    'name': "Farooq Fabrics",

    'summary': """
        We the Farooq Fabrics have all types of Ladies suites.
        """,

    'description': """
        This module is about the management system of Fabrics Shop.
    """,

    'author': "Farooq Butt",
    'website': "http://farooqfabrics.com",
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory System',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'demo' : [],
    'qweb' : [],
    'installable' : True,
    'application' : True,
    'auto_install' : False
}
