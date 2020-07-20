from openerp import models, fields


class Production(models.Model):
    _inherit = 'mrp.production'

    product_id = fields.Many2one('product.product', string='Products', domain=[('sale_ok', '==', True)])
    date = fields.Datetime(required=True)
    number = fields.Integer()
    reference = fields.Char(required=True)
    material = fields.Char(required=True)
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
    ], default='creation', required=True)
    number_of_pages = fields.Integer()
    total_weight = fields.Float()
    loss = fields.Float()
    palette_quantity = fields.Integer()
    laize_quantity = fields.Integer()

    customer_ids = fields.One2many('res.partner', 'production_id', string='customers', domain=[('customer', '=', True)])
    color1 = fields.Boolean()
    color2 = fields.Boolean()
    color3 = fields.Boolean()
    color4 = fields.Boolean()
    color5 = fields.Boolean()
    option1 = fields.Boolean()
    option2 = fields.Boolean()
    option3 = fields.Boolean()
    option4 = fields.Boolean()
    option5 = fields.Boolean()


class Partner(models.Model):
    _inherit = 'res.partner'

    production_id = fields.Many2one('mrp.production', domain=[('customer', '=', True)])
