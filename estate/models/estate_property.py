from dateutil.relativedelta import relativedelta
from odoo import api, fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property"

    # Model's fields
    name = fields.Char(string='Title', required=True, translate=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
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

    user_id = fields.Many2one('res.users', string="Salesman", index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer', "property_id")
    total_area = fields.Integer(string="Total Area (sqm)", compute="_compute_total")
    best_price = fields.Float(string="Best Offer", compute="_compute_best_offer")
    create_date = fields.Date(string="Create Date", readonly=True)

    @api.depends("garden_area", "living_area")
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_offer(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped("price")) if record.offer_ids else 0.0

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

