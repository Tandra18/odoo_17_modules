from odoo import fields, models, api
import re


class Sponsor(models.Model):
    _name = 'event.sponsor'
    _description = 'Event Sponsor'
    _table = 'sponsor'

    name = fields.Char(string="Name", required=True)
    image = fields.Binary(string="Logo", required=True)
    event_id = fields.Many2one('event.management', string="Event", required=True)
    reg_date = fields.Date(string="Agreement Date", required=True)
    website = fields.Char(string="Website", required=True)

    contact_person = fields.Char(string="Contact Person", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone", required=True)
    address = fields.Char(string="Address", required=True)

    level = fields.Selection(
        [
            ('bronze', 'Bronze'),
            ('silver', 'Silver'),
            ('gold', 'Gold'),
            ('platinum', 'Platinum'),
        ], string="Level", required=True
    )
    amount_contributed = fields.Integer(string="Amount Contributed")
    payment_status = fields.Selection(
        [
            ('pending', 'Pending'),
            ('partial', 'Partially Paid'),
            ('paid', 'Paid'),
        ], string="Payment"
    )
    support = fields.Text(string="In Kind Support")

    note = fields.Text(string="Notes")


