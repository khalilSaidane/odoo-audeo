
from openerp import models, fields, api


class CheckListHistory(models.Model):
    _inherit = ['cmms.checklist.history']

    equipment_type = fields.Char(related='equipment_id.type')