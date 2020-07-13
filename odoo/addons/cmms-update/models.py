# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import osv


class Incident(models.Model):
    _inherit = 'cmms.incident'
#   ref = fields.Reference(domain=[('create_uid','=','self.env.user')])

# @api.onchange('ref')
#   def _on_ref_selected(self):
#      for rec in self:
#        if rec.ref:
#               print(self.ref.create_uid.id == self.env.user.id)
#               return {'domain': {'ref': [('create_uid.id','=',self.env.user.id)]}}

    def action_done(self, cr, uid, ids, context=None):
        self.action_broadcast(cr,uid,ids,context)
        return super(Incident, self).action_done(cr,uid,ids)

    """email"""

    def action_broadcast(self, cr, uid, ids, context={}):
        data_email = []
        text_inter = u"""<div style="font-family: 'Lucica Grande', Ubuntu, Arial, Verdana, sans-serif; font-size: 12px; color: rgb(34, 34, 34); background-color: rgb(255, 255, 255); ">
                    <p>Bonjour %s, </p>
                    <p>Nous vous informons que le bon de travail %s a été validé par  %s.</p>
                    <br/>
                    <p></p>
                    <p>-----------------------------</p>
                    <p>Référence bon de travail   : %s </p>
                    <p>Priorité : %s </p>
                    <p>Origine bon de travail  : %s </p>
                    <p>Date bon de travail  : %s </p>
                    <p>------------------------------</p>
                    <p> Service du Gmao</p>
                    </div>
                    """
        for object_inter in self.browse(cr, uid, ids):
            if not object_inter.create_uid.login:
                raise osv.except_osv(u'Email non spécifiée', u'Veuillez indiquer l\'email de Destinataire')
            if object_inter.create_uid.login:
                text_inter = text_inter % (
                    object_inter.create_uid.name,
                    object_inter.name, object_inter.create_uid.name,
                    object_inter.name,
                    object_inter.priority,
                    object_inter.ref,
                    object_inter.date,

                )
                data_email.append(
                    {
                        'subject': "Service du Gmao %s" % object_inter.name,
                        'email_to': object_inter.create_uid,
                        'subtype': 'html',
                        'body_text': False,
                        'body_html': text_inter,
                    }
                )

        self.pool.get('cmms.parameter.mail').send_email(cr, uid, data_email, module='cmms', param='cmms_event_mail')


"""fin"""