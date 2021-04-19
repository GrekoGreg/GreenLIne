# coding: utf-8

{
    'name': "CAP MRP Workcenter Stage",
    'author': 'Captivea',
    'website': 'www.captivea.us',
    'version': '14.1.1.0.0',
    'category': 'MRP',
    'summary': """display a MRP workcenter knaban view by stages.""",
    'license': 'AGPL-3',
    'description': """display a MRP workcenter knaban view by stages.""",
    'depends': ['mrp'],
    'data': [
        'views/mrp_workcenter_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
