# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime
from datetime import timedelta


class PM(models.Model):
    _inherit = ['cmms.pm']

    equipment_type = fields.Char(related='equipment_id.type', string='Référence machine')
    graissage = fields.Boolean()
    lubrification = fields.Boolean()
    vidange = fields.Boolean()


    @api.model
    def send_reminder_mails(self):
        pms = self.env['cmms.pm'].search([])
        for pm in pms:
            d = datetime.strptime(pm.days_next_due, '%Y-%m-%d') - timedelta(days=pm.days_warn_period)
            if d.date() == datetime.now().date():
                self.action_broadcast(pm=pm)

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

    def get_str_types(self):
        str_types = ''
        for rec in self:
            if rec.graissage:
                str_types += 'Graissage '
            if rec.lubrification:
                str_types += 'Lubrification '
            if rec.vidange:
                str_types += 'Vidange '
        return str_types

    def action_broadcast(self, cr, uid, pm, context={}):
        data_email = []
        text_inter = u"""<div style="font-family: 'Lucica Grande', Ubuntu, Arial, Verdana, sans-serif; font-size: 12px; color: rgb(34, 34, 34); background-color: rgb(255, 255, 255); ">
                        <p>Bonjour, </p>
                        <p>Nous vous informons que vous avez une maintenance préventive %s créée par %s.</p>
                        <br/>
                        <p></p>
                        <p>-----------------------------</p>
                        <p>Ref maintenance préventive   : %s </p>
                        <p>Machine : %s </p>
                        <p>Référence machine  : %s </p>
                        <p>Type  : %s </p>
                        <p>Prochaine date   : %s </p>
                        <p>------------------------------</p>
                        <p> Service du Gmao</p>
                        <p> %s </p>
                        </div>
                        """

        text_inter = text_inter % (
            pm.name, pm.create_uid.name,
            pm.name,
            pm.equipment_id.name,
            pm.equipment_id.type,
            pm.get_str_types(),
            pm.days_next_due,
            pm.env.user.company_id.name,
        )
        data_email.append(
            {
                'subject': "Service du Gmao %s" % pm.name,
                'email_to': pm.env.user.company_id.email,
                'subtype': 'html',
                'body_text': False,
                'body_html': text_inter,
                'email_cc': pm.get_managers_email()
            }
        )

        self.pool.get('cmms.parameter.mail').send_email(cr, uid, data_email, module='cmms', param='cmms_event_mail')


"""fin"""
