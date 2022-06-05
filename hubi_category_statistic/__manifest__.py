# -*- coding: utf-8 -*-
{
    'name': "hubi_category_statistic",

    'summary': """
        hubi_category_statistic""",

    
    'author': "Difference informatique - MIADI",
   
    'category': 'HUBI',
    'version': '14',

    # any module necessary for this one to work correctly
      'depends': [  
          'base', 'base_setup', 'product'
                                        
        ],

    # always loaded
    'data': [
        
        "wizards/wiz_update_stats_views.xml",
        "views/partner_product_category_views.xml",
        "security/ir.model.access.csv",
        #"views/inh_parameter_config_views.xml",         
     ],
    # only loaded in demonstration mode
    'demo': [
       
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'OPL-1',
}