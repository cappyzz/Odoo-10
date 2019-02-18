# -*- coding: utf-8 -*-

from openerp import http
from openerp.http import request
from openerp.addons.web.controllers.main import serialize_exception,content_disposition
import base64, os, inspect, logging

_logger = logging.getLogger()


class outlook_download(http.Controller):
    @http.route('/web/binary/download_outlook_add_in', type='http', auth="user")
    def download_outlook_add_in(self, debug=None):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, '..', 'bin', 'OutlookAddInInstaller.exe'), 'rb') as installer:
            db = request.db
            base_url = request.env['ir.config_parameter'].get_param('web.base.url')
            return request.make_response(installer.read(),
                            [('Content-Type', 'application/octet-stream'),
                             ('Content-Disposition', content_disposition('OutlookAddInInstaller.exe'))])
