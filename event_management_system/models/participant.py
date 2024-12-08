from odoo import fields, models, api


class participants(models.Model):
    _name = 'event.participants'
    _description = 'Event Participants'
    _table = 'participants'

    image = fields.Binary(string="Image", required=True)
    name = fields.Char(string='Name', required=True)
    nrc = fields.Char(string='NRC', required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Integer(string="Phone Number", required=True)
    event_id = fields.Many2one('event.management', string='Event', required=True)
    reg_date = fields.Date(string='Registration Date', default=fields.Datetime.now)
    payment = fields.Selection(
        [
            ('kpay', 'KBZ Pay'),
            ('wave', 'Wave Pay'),
            ('ayapay', 'AYA Pay'),
            ('cbpay', 'CB Pay'),
            ('awallet', 'A+ Wallet'),
        ], string="Choose Payment Type"
    )

    # _sql_constraints = ('email_unique', 'unique(email)', 'Participant Email must be unique!')
