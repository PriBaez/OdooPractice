from dateutil.relativedelta import relativedelta
from odoo import api, fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property\'s Offers"

    # model/table fields
    price = fields.Float(string='Price')
    status = fields.Selection(string='Status', copy=False, selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', required=True)
    create_date = fields.Date(string="Create Date", readonly=True)
    validity = fields.Integer(string='Validity(days)', default=7)
    date_deadline = fields.Date(string='Deadline', compute="_compute_deadline", inverse="_inverse_deadline")

    @api.depends("validity")
    def _compute_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta(days=record.validity)

    @api.onchange("date_deadline")
    def _inverse_deadline(self):
        validity_days = self.date_deadline - self.create_date
        self.validity = validity_days.days
