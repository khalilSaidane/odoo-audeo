# -*- coding: utf-8 -*-
from openerp import http

# class Stock-update(http.Controller):
#     @http.route('/stock-update/stock-update/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock-update/stock-update/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock-update.listing', {
#             'root': '/stock-update/stock-update',
#             'objects': http.request.env['stock-update.stock-update'].search([]),
#         })

#     @http.route('/stock-update/stock-update/objects/<model("stock-update.stock-update"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock-update.object', {
#             'object': obj
#         })