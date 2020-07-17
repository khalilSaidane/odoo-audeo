# -*- coding: utf-8 -*-

from openerp import models, fields, api


class CM(models.Model):
    _inherit = ['cmms.cm']

    equipment_type = fields.Char(related='equipment_id.type', string='Référence machine')

    @api.model
    def create(self, vals):
        vals['use_id'] = self.env.uid
        return super(CM, self).create(vals)