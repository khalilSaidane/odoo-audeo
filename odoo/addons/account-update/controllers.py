# -*- coding: utf-8 -*-
from openerp import http

# class Account-update(http.Controller):
#     @http.route('/account-update/account-update/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account-update/account-update/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account-update.listing', {
#             'root': '/account-update/account-update',
#             'objects': http.request.env['account-update.account-update'].search([]),
#         })

#     @http.route('/account-update/account-update/objects/<model("account-update.account-update"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account-update.object', {
#             'object': obj
#         })