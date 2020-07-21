from openerp import models, fields


class Production(models.Model):
    _inherit = 'mrp.production'

    reference = fields.Char(required=True, string='Referance interne')
    material = fields.Many2one('product.template', domain=[('categ_id.name', '=', 'Matiere Consommable')])
    weight = fields.Float(required=True)
    unit_dimension = fields.Float(required=True)
    width = fields.Float()
    height = fields.Float()
    number_of_poses = fields.Integer()
    state1 = fields.Selection([
        ('creation', 'Creation'),
        ('repetition', 'Repetition'),
        ('encours', 'Encours'),
        ('partiellement delivrer', 'Partiellement Delivrer'),
        ('terminer', 'Terminer'),
    ], default='creation', required=True, string='etat')
    number_of_pages = fields.Integer()
    total_weight = fields.Float()
    loss = fields.Float()
    palette_quantity = fields.Integer()
    laize_quantity = fields.Integer()

    customer_ids = fields.Many2one('res.partner',domain=[('customer', '=', True)])

    color_ids = fields.Many2many('production.color')
    option_ids = fields.Many2many('production.option')


    class Color(models.Model):
        _name = 'production.color'

        name = fields.Char(string='Couleur')
    class Option(models.Model):
        _name = 'production.option'

        name = fields.Char(string='Option')
