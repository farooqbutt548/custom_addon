# -*- coding: utf-8 -*-
{
    'name': "Attendance Analysis",

    'summary': """
        Attendance Analysis of Employees""",

    'description': """
        This module contains Analysis records of Employees. 
    """,

    'author': "Cybat Tech",
    'website': "http://www.cybat.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Attendance Analysis',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_attendance'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/attendance_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
