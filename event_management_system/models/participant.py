import re

from odoo import fields, models, api, exceptions


class participants(models.Model):
    _name = 'event.participants'
    _description = 'Event Participants'
    _table = 'participants'

    image = fields.Binary(string="Image", required=True)
    age = fields.Integer(string="Age", required=True)
    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
        ], string="Gender", required=True
    )
    name = fields.Char(string='Name', required=True)
    nrc = fields.Char(string='NRC', required=True)
    address = fields.Char(string="Address", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone Number", required=True)
    event_id = fields.Many2one('event.management', string='Event', required=True)
    reg_date = fields.Date(string='Registration Date', default=fields.Datetime.now)
    fees = fields.Integer(string="Fees")
    payment = fields.Selection(
        [
            ('kpay', 'KBZ Pay'),
            ('wave', 'Wave Pay'),
            ('ayapay', 'AYA Pay'),
            ('cbpay', 'CB Pay'),
            ('awallet', 'A+ Wallet'),
        ], string="Choose Payment Type"
    )

    @api.constrains('phone')
    def _check_hotline_number(self):
        for record in self:
            if record.phone:
                if not re.match(r'^\d{9,11}$', record.phone):
                    raise exceptions.ValidationError("Phone number must be a numeric value between 9 and 11 digits!")

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email:
                if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',record.email):
                    raise exceptions.ValidationError("Please enter a valid email address!")

    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age < 10 or record.age > 99:
                raise exceptions.ValidationError("Age must be between 10 to 99!")

    @api.onchange('event_id')
    def _onchange_event_id(self):
        if self.event_id:
            # Copy the 'amount' value from the selected event to the 'fees' field
            self.fees = self.event_id.amount

    # _sql_constraints = ('email_unique', 'unique(email)', 'Participant Email must be unique!')
