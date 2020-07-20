# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import osv
from datetime import datetime
AVAILABLE_PRIORITIES_FR = {
    '3':'Normal',
    '2':'Basse',
    '1':'Haute'
}



class Incident(models.Model):
    _inherit = ['cmms.incident']
    # replacing the ref field with a selection request_link field and 4 many to one fields
    #  in order to add specific domains to every field
    request_link = fields.Selection([
        ('cmms.cm', 'Maintenance corrective'),
        ('cmms.pm', 'Maintenance préventive'),
        ('cmms.checklist.history', 'Liste de contrôle'),
        ('cmms.intervention', 'Demande d intervention'),
    ], string="Type de document")

    cm_id = fields.Many2one('cmms.cm',
                            string='Maintenance corrective',
                            domain=lambda self: [('create_uid', '=', self.env.uid)] if 'cmms-manager' not in [g.name for g in self.env.user.groups_id] else None)
    pm_id = fields.Many2one('cmms.pm',
                            string='Maintenance préventive',
                            domain=lambda self: [('create_uid', '=', self.env.uid)] if 'cmms-manager' not in [g.name for g in self.env.user.groups_id] else None)
    checklist_history_id = fields.Many2one('cmms.checklist.history',
                                           string='Liste de contrôle')
    intervention_id = fields.Many2one('cmms.intervention',
                                      string='Demande d intervention',
                                      domain=lambda self: [('user2_id', '=', self.env.uid)] if 'cmms-manager' not in [g.name for g in self.env.user.groups_id] else None)
    equipment_type = fields.Char(related='equipment_id.type', string='Référence machine')

    # Dynamically selecting the machine based on the document selected
    @api.onchange('cm_id')
    def cm_id_on_change(self):
        for rec in self:
            if rec.cm_id:
                rec.equipment_id = rec.cm_id.equipment_id
                rec.pm_id = None
                rec.checklist_history_id = None
                rec.intervention_id = None

    @api.onchange('pm_id')
    def pm_id_on_change(self):
        for rec in self:
            if rec.pm_id:
                rec.equipment_id = rec.pm_id.equipment_id
                rec.cm_id = None
                rec.checklist_history_id = None
                rec.intervention_id = None

    @api.onchange('checklist_history_id')
    def checklist_history_id_on_change(self):
        for rec in self:
            if rec.checklist_history_id:
                rec.equipment_id = rec.checklist_history_id.equipment_id
                rec.pm_id = None
                rec.cm_id = None
                rec.intervention_id = None

    @api.onchange('intervention_id')
    def intervention_id_on_change(self):
        for rec in self:
            if rec.intervention_id:
                rec.equipment_id = rec.intervention_id.equipment_id
                rec.pm_id = None
                rec.checklist_history_id = None
                rec.cm_id = None

    def _get_document(self):
        """
        Every incident must have only one document attached
        :return: the document cm, pm, checklist_history, or intervention
        """
        for rec in self:
            if rec.cm_id:
                return rec.cm_id
            if rec.pm_id:
                return rec.pm_id
            if rec.checklist_history_id:
                return rec.checklist_history_id
            if rec.intervention_id:
                return rec.intervention_id

    def action_done(self, cr, uid, ids, context=None):
        """
        Send an email to the responsible before validating
        """
        self.action_broadcast(cr, uid, ids, context)
        return super(Incident, self).action_done(cr, uid, ids)

    def get_managers_email(self, cr, uid, context={}):
        obj = self.pool.get('res.groups')
        ids = obj.search(cr, uid, [('name', '=', 'cmms-manager')])
        res = obj.read(cr, uid, ids, ['users'], context)
        res = res[0]['users']
        manager_ids = [id for id in res]
        managers = self.pool.get('res.users').browse(cr, uid, manager_ids)
        emails = [manager.login for manager in managers]
        formatted_emails = ''
        for email in emails:
            if email:
                formatted_emails += email + ' ;'

        return formatted_emails

    """email"""

    def action_broadcast(self, cr, uid, ids, context={}):
        data_email = []
        text_inter = u"""<div style="font-family: 'Lucica Grande', Ubuntu, Arial, Verdana, sans-serif; font-size: 12px; color: rgb(34, 34, 34); background-color: rgb(255, 255, 255); ">
                    <p>Bonjour, </p>
                    <p>Nous vous informons que le bon de travail %s a été validé par  %s.</p>
                    <br/>
                    <p></p>
                    <p>-----------------------------</p>
                    <p>Référence bon de travail   : %s </p>
                    <p>Priorité : %s </p>
                    <p>Origine bon de travail  : %s </p>
                    <p>Machine  : %s </p>
                    <p>Reference du machine  : %s </p>
                    <p>Date bon de travail  : %s </p>
                    <p>Date de validation  : %s </p>
                    <p>------------------------------</p>
                    <p> Service du Gmao</p>
                    <p> %s </p>
                    </div>
                    """
        for object_inter in self.browse(cr, uid, ids):
            if not object_inter.create_uid.login:
                raise osv.except_osv(u'Email non spécifiée', u'Veuillez indiquer l\'email de Destinataire')
            if object_inter.create_uid.login:
                text_inter = text_inter % (
                    object_inter.name, object_inter.create_uid.name,
                    object_inter.name,
                    AVAILABLE_PRIORITIES_FR.get(str(object_inter.priority)),
                    object_inter._get_document().name,
                    object_inter._get_document().equipment_id.name,
                    object_inter._get_document().equipment_id.type,
                    object_inter.date,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    object_inter.env.user.company_id.name,
                )
                data_email.append(
                    {
                        'subject': "Service du Gmao %s" % object_inter.name,
                        'email_to': object_inter.env.user.company_id.email,
                        'subtype': 'html',
                        'body_text': False,
                        'body_html': text_inter,
                        'email_cc': object_inter.get_managers_email()
                    }
                )

        self.pool.get('cmms.parameter.mail').send_email(cr, uid, data_email, module='cmms', param='cmms_event_mail')

"""fin"""
