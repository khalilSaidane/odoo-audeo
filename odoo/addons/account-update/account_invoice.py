from openerp import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    production_id = fields.Many2one('mrp.production', domain=[('product_id', '=', 'product_id')])
    ok = fields.Boolean()