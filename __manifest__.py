# servicio_manteminiento/__manifest__.py
{
'name': 'Servicio de Mantenimiento',
'version': '1.0',
'author': 'Paco Navas',
'category': 'Custom',
'summary': 'Gestión de Mantenimiento de Productos',
'depends': ['base', 'garantias'],
'data': [
'security/ir.model.access.csv',
'views/servicio_mantenimiento_views.xml',
],
'icon': '/garantias/static/description/icon55.png',
'installable': True,
'application': True,
}