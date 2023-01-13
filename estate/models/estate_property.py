from dateutil.relativedelta import relativedelta
from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property"

    name = fields.Char(string='Title', required=True, translate=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Available From', copy=False,
                                    default=(fields.Datetime.now() + relativedelta(months=3)))
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(default=False, string='Garage')
    garden = fields.Boolean(default=False, string='garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(string='Garden Orientation',
                                          selection=[('north', 'North'),
                                                     ('south', 'South'), ('east', 'East'), ('west', 'West')]
                                          )
    active = fields.Boolean(string='It\'s Active?', default=True)
    state = fields.Selection(string="Property\'s State",
                             selection=[('new', 'New'), ('offer received', 'Offer Received'),
                                        ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'),
                                        ('canceled', 'Canceled')], default='new'
                             )
