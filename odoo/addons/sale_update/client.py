# -*- coding: utf-8 -*-

from openerp import models, fields


class Client(models.Model):
    _inherit = 'res.partner'

    type_id = fields.Many2one('res.partner.type')
    ok = fields.Boolean()


class ClientType(models.Model):
    _name = 'res.partner.type'

    name = fields.Char(string='Niveau client')

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "Le nom doit etre unique"),
    ]