from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tags For Estate Property records"
    _order = 'name'

    name = fields.Char(string="Tag", required=True)
    color = fields.Integer()

    _sql_constraints = [('tag_unique', 'UNIQUE (name)',
                        'The name must be unique')
                        ]
