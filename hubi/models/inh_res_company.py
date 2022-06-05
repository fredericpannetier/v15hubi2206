# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
   
class HubiResCompany(models.Model):
    _inherit = 'res.company'
    
    di_bottom_message_invoice = fields.Text(string="Bottom message invoice", related='partner_id.di_bottom_message_invoice')
    di_bottom_message_delivery = fields.Text(string="Bottom message delivery", related='partner_id.di_bottom_message_delivery')