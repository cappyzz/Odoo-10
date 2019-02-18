# -*- coding: utf-8 -*-

from openerp import models, fields, api


class outlook_sync(models.Model):
    _name = 'odoo_outlook.outlook_sync'
    
    def _server(self):
        return self.env['ir.config_parameter'].get_param('web.base.url')
    server = fields.Char(readonly=True, default=_server)
    
    def _database(self):
        return self.env.cr.dbname
    database = fields.Char(readonly=True, default=_database)
    
    @api.multi
    def download_outlook(self):
        return {
            'type' : 'ir.actions.act_url',
            'url': '/web/binary/download_outlook_add_in',
            'target': 'self',
        }

