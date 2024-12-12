from odoo import fields, api, models


class Agreement(models.Model):
    _name = 'sponsor.agreement'
    _description = 'Sponsor Agreement'
    _table = 'sponsor_agreement'

    event_id = fields.Many2one('event.management',string="Event Name")
    sponsor_id = fields.Many2one('event.sponsor', string="Sponsor Name")

