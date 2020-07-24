# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Intervention(models.Model):
    _inherit = ['cmms.intervention']

    equipment_type = fields.Char(related='equipment_id.type',string='Référence machine')

