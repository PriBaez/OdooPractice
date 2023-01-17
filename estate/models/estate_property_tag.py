from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tags For Estate Property records"

    name = fields.Char(string="Tag", required=True)
