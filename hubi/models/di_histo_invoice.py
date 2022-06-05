# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
       
class HubidiHistoInvoice(models.Model):
    _name = "di.histo.invoice"
    _description = "Archived Invoice"
    _order = "num_invoice"

    type_invoice = fields.Selection([('F', "invoice"),('A', "credit note"),        ],
        default='F', string='Type Invoice'  )
    num_invoice = fields.Char(string='Num Invoice')
    date_invoice = fields.Date(string='Date Invoice')
    partner_id = fields.Many2one('res.partner', string='Partner')
    partner_ref = fields.Char(string='Reference Partner')

    categ_id = fields.Many2one('product.category', 'Product Category', help="Select category for the current product")
    caliber_id = fields.Many2one('di.multi.table', string='Caliber', domain=[('record_type', '=', 'Caliber')], help="The Caliber of the product.")
    packaging_id = fields.Many2one('di.multi.table', string='Packaging', domain=[('record_type', '=', 'Packaging')], help="The Packaging of the product.")
    
    quantity = fields.Float('quantity')
    weight = fields.Float('Weight')
    weight_total = fields.Float('Weight Total')
    price_unit = fields.Float('Price Unit')
    price_unit_weight = fields.Float('Price Unit Weight')
    amount_total = fields.Float('Amount Total')
    

       
