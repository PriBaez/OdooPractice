from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property\'s Offers"
    _order = 'price desc'

    # model/table fields
    price = fields.Float(string='Price')
    status = fields.Selection(string='Status', copy=False, selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', required=True, string="")
    create_date = fields.Date(string="Create Date", readonly=True)
    validity = fields.Integer(string='Validity(days)', default=7)
    date_deadline = fields.Date(string='Deadline', compute="_compute_deadline", inverse="_inverse_deadline")
    property_type_id = fields.Many2one('estate.property.type', related='property_id.property_type_id',
                                       string="Property Type", store=True)

    @api.depends("validity")
    def _compute_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = datetime.now() + relativedelta(days=record.validity)

    @api.onchange("date_deadline")
    def _inverse_deadline(self):
        for record in self:
            if record.create_date:
                validity_days = record.date_deadline - record.create_date
                record.validity = validity_days.days
            else:
                validity_days = record.date_deadline - datetime.now().date()
                record.validity = validity_days.days

    # Button actions
    @api.depends("partner_id")
    def action_accept(self):
        for record in self:
            if record.status != 'accepted':
                record.status = 'accepted'
                record.mapped("property_id").write(
                    {
                        "state": "offer accepted",
                        "selling_price": self.price,
                        "buyer_id": self.partner_id.id
                    }
                )
            else:
                raise UserError('Only one offer can be accepted')

    def action_refuse(self):
        for record in self:
            if record.status != 'refused':
                record.status = 'refused'
            else:
                raise UserWarning("That offer is already refused")

    _sql_constraints = [('offer_price_positive', 'CHECK(price > 0)',
                         'The Offer price must be strictly positive')
                        ]

    @api.model
    def create(self, vals_list):
        estate_property_record = self.env['estate.property'].browse(vals_list["property_id"])
        estate_property_record.state = 'offer received'

        if vals_list['price'] < estate_property_record.best_price:
            raise UserError("The offer must be higher than " + str(estate_property_record.best_price))

        return super().create(vals_list)
