from openerp import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice.line'

    production_id = fields.Many2one('mrp.production')

    @api.onchange('product_id', 'production_id')
    def _on_product_change(self):
            for rec in self:
                return {'domain':{'production_id': [('bom_id.product_id', '=', rec.product_id.id)]}}
