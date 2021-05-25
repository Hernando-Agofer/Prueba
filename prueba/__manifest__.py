# -*- coding: utf-8 -*-
{
    'name': "prueba",

    'summary': "Pruebas Reyes Santana",

    'description': "Pruebas Reyes Santana",

    'author': "Reyes Hernando Santana",
    'website': "inghernandosan@outlook.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/group.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
