# -*- coding: utf-8 -*-

from openerp import models, fields, api


class CM(models.Model):
    _inherit = ['cmms.cm']

    equipment_type = fields.Char(related='equipment_id.type', string='Référence machine')
