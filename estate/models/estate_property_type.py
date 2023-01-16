from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Type/Sort of property\'s on sale"

    name = fields.Char(string='Property\'s Type', required=True)

