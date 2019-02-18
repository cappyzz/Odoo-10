# -*- coding: utf-8 -*-
{
    'name': "Odoo Outlook Add-In",

    'summary': """
        An Odoo connector add-in for Microsoft Outlook.
        """,

    'description': """
        The Outlook add-in allows the user to connect Odoo and Outlook. Synchronisation is bi-directional and the user may decide which direction to prioritize (Odoo or Outlook)
    """,

    'author': "Atteli - Juliusz Sosinowicz",
    'website': "http://atteli.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Customer Relationship Management',
    'version': '0.1',

    # License
    'license': 'GPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'project'],

    # always loaded
    'data': [
        'views/outlook.xml',
        'records/ir.model.access.csv',
    ],

    'qweb': [
        'views/templates.xml',
    ],
    'images': [
        'static/description/oregano.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}