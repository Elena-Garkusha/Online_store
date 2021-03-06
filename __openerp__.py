{
    'name': "online_store",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'vendors/jquery/dist/jquery.min.js',
        # 'vendors/bootstrap/dist/js/bootstrap.min.js',
        # 'vendors/fastclick/lib/fastclick.js',
        # 'vendors/nprogress/nprogress.js',
        # 'vendors/jQuery-Smart-Wizard/js/jquery.smartWizard.js',
        # 'build/js/custom.min.js',
        # 'static/smile.jpg',
        'views/templates.xml',
        # 'views/views.xml',
        # 'views/assets.xml',
        # 'views/page2.xml',
        'views/login_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
# -*- coding: utf-8 -*-
