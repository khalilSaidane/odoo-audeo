# -*- coding: utf-8 -*-

from openerp import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    category_id = fields.Many2one('product.template.category')

    _sql_constraints = [
        ('default_code_unique',
         'UNIQUE(default_code)',
         "La reference interne doit etre unique"),
    ]


class ProductCategory(models.Model):
    _name = 'product.template.category'

    name = fields.Char(string='Category')

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "Le nom doit etre unique"),
    ]
