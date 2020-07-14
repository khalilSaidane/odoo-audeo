# -*- coding: utf-8 -*-

from openerp import models, fields


class PM(models.Model):
    _inherit = ['cmms.pm']

    equipment_type = fields.Char(related='equipment_id.type',string='Référence machine')

    graissage = fields.Boolean()
    lubrification = fields.Boolean()
    vidange = fields.Boolean()

