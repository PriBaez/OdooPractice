from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Type/Sort of property\'s on sale"
    _order = 'name'

    name = fields.Char(string='Property\'s Type', required=True)
    sequence = fields.Integer('Sequence', default=1, help='Used for order Types of property manually.')
    property_ids = fields.One2many("estate.property", "property_type_id")

    _sql_constraints = [('estate_type_unique', 'UNIQUE (name)',
                        'The name must be unique')
                        ]
