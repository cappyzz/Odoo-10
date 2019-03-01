# -*- coding: utf-8 -*-
# Copyright 2017-2018 Naglis Jonaitis
# License AGPL-3 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'OpenProject Connector',
    'version': '10.0.2.0.2',
    'author': 'Naglis Jonaitis',
    'category': 'Connector',
    'website': 'https://naglis.me/',
    'license': 'AGPL-3',
    'summary': 'Synchronize OpenProject with Odoo',
    'external_dependencies': {
        'python': [
            'isodate',
            'requests',
            'requests_mock',
            'slugify',
        ],
    },
    'depends': [
        'connector',
        'hr_timesheet',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'data/mail_message_subtype.xml',
        'data/res_partner.xml',
        'views/backend.xml',
        'views/openproject_account_analytic_line.xml',
        'views/openproject_res_users.xml',
        'views/openproject_project_task.xml',
        'views/openproject_project_project.xml',
    ],
    'demo': [
        'demo/openproject.xml',
    ],
    'images': [
        'static/description/main_screenshot.png',
    ],
    'installable': True,
    'application': True,
}
