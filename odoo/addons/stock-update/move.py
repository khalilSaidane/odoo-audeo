from openerp import models, fields, api


class Move(models.Model):
    _inherit = 'stock.move'

    production_id = fields.Many2one('mrp.production')

    @api.onchange('product_uom')
    def onchange_product_uom(self):
        for rec in self:
            return {'domain': {'production_id': [('product_id', '=', rec.product_id.id)]}}