# See LICENSE file for full copyright and licensing details.

{
    'name': 'Partner Total Due',
    'version': '15.0.1.0.0',
    'category': 'difmiadi',
    
    'author': 'Difference informatique - MIADI',
    
    'summary': 'Display the total due of the customer',
    'depends': [
        'base', 'account',
    ],
    'data': [
       'views/inh_partner_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
}
