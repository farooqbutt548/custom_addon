# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Open Academy is a Module to learn Odoo-13 for internship""",

    'description': """
        Open Academy is a Module to learn Odoo-13 for internship
    """,

    'author': "Farooq Butt",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'bilal_fabrics'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/openacademy_session.xml',
        'views/bilal_fabrics_inherit_view.xml',
        'views/car_inherits_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
