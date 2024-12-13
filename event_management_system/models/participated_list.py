from odoo import fields, models, api, exceptions


class ParticipatedList(models.Model):
    _name = 'participated.list'
    _description = 'Participated List'
    _table = 'participated_list'

    event_id = fields.Many2one('event.management', string="Event Name", required=True)
    participant_id = fields.Many2one('event.participant', string="Participant Name", required=True)
    agreed_date = fields.Date(string="Agreement Date", required=True)

    payment_status = fields.Selection(
        [
            ('pending', 'Pending'),
            ('partial', 'Partially Paid'),
            ('paid', 'Paid'),
        ], string="Payment Status", required=True
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('done', 'Done'),
            ('confirm', 'Confirmed'),
            ('cancel', 'Canceled'),
        ], string="Status", default="draft", tracking=True
    )

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_confirm(self):
        for record in self:
            record.state = 'confirm'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_cancel(self):
        for record in self:
            record.state = 'cancel'


