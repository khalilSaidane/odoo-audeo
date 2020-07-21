# -*- coding: utf-8 -*-
from openerp import http

# class Cmms-update(http.Controller):
#     @http.route('/cmms-update/cmms-update/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cmms-update/cmms-update/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cmms-update.listing', {
#             'root': '/cmms-update/cmms-update',
#             'objects': http.request.env['cmms-update.cmms-update'].search([]),
#         })

#     @http.route('/cmms-update/cmms-update/objects/<model("cmms-update.cmms-update"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cmms-update.object', {
#             'object': obj
#         })