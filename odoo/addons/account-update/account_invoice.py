from openerp import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice.line'

    production_id = fields.Many2one('mrp.production')

    @api.onchange('name')
    def onchange_name(self):
        for rec in self:
            return {'domain': {'production_id': [('product_id', '=', rec.product_id.id)]}}