

{
    'name': "estate",
    'depends': ['base'],
    'License': "LGPL-3",
    'author': "Prisila Baez Mendez",
    'category': 'My Addons',
    'application': True,
    'description': "Real Estate module",

    'data': [
        './views/estate_property_views.xml',
        './views/estate_menus.xml',
        './views/estate_type_views.xml',
        './security/ir.model.access.csv'
    ],
    'css': ['static/src/Property.css']
}

