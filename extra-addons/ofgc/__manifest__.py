# -*- coding: utf-8 -*-
{
    'name': "OFGC",

    'summary': """
        Calendar for OFGC's musicians """,

    'description': """
         Calendar for OFGC's musicians where they can see their projects
        and events. We decided to put 5 menus of the original application because we think that those
        are the most importants:\n
        - Seasons submenu, for example winter.\n
        - Projects submenu, this is the most important and central one, because every musicians will
        have x number of projects with their own events. When everything is finished, the project is finished.\n
        - Schedule submenu, is an event of a project.\n
        - The type of schedule submenu, its own name explains it.\n
        The room where the schedule will take place)
    """,

    'author': "Isaiah Jesús Martel Martín",
    'website': "https://github.com/IsaiahMartel",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'prt_report_attachment_preview', 'web_responsive'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/season_report.xml',
        'reports/seasons_report_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': 'True',
}
