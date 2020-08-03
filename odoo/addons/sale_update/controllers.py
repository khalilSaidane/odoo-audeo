# -*- coding: utf-8 -*-
from openerp import http

# class SaleUpdate(http.Controller):
#     @http.route('/sale_update/sale_update/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_update/sale_update/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_update.listing', {
#             'root': '/sale_update/sale_update',
#             'objects': http.request.env['sale_update.sale_update'].search([]),
#         })

#     @http.route('/sale_update/sale_update/objects/<model("sale_update.sale_update"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_update.object', {
#             'object': obj
#         })