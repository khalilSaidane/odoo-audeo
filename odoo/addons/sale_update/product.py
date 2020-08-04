# -*- coding: utf-8 -*-

from openerp import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    _sql_constraints = [
        ('default_code_unique',
         'UNIQUE(default_code)',
         "La reference interne doit etre unique"),
    ]
