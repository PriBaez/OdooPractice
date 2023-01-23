from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Type/Sort of property\'s on sale"

    name = fields.Char(string='Property\'s Type', required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")

    _sql_constraints = [('estate_type_unique', 'UNIQUE (name)',
                        'The name must be unique')
                        ]
