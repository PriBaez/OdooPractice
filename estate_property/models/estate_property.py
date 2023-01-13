from dateutil.relativedelta import relativedelta
from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property"

    name = fields.Char(string='Property\'s Name', required=True, translate=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date\'s availability', copy=False,
                                    default=(fields.Datetime.now() + relativedelta(months=3)))
    expected_price = fields.Float(string='Expected price', required=True)
    selling_price = fields.Float(string='Selling price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Number of bedrooms', default=2)
    living_area = fields.Integer(string='number of living area')
    facades = fields.Integer(string='number of facades')
    garage = fields.Boolean(default=False, string='Has a garage?')
    garden = fields.Boolean(default=False, string='Has a garde?')
    garden_area = fields.Integer(string='Number of garden')
    garden_orientation = fields.Selection(string='Garden orientation',
                                          selection=[('north', 'North'),
                                                     ('south', 'South'), ('east', 'East'), ('west', 'West')]
                                          )
    active = fields.Boolean(string='The record is active', default=True)
    state = fields.Selection(string="state of the property",
                             selection=[('new', 'New'), ('offer received', 'Offer Received'),
                                        ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'),
                                        ('canceled', 'Canceled')], default='new'
                             )
