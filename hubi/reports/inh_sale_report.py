# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import tools
from odoo import fields, models


class HubiSaleReport(models.Model):
    _inherit = "sale.report"

    carrier_name = fields.Char('Carrier Name', readonly=True)
    category_name = fields.Char('Category Name', readonly=True)
    caliber_name = fields.Char('Caliber Name', readonly=True)
    packaging_name = fields.Char('Packaging Name', readonly=True)
    
    packaging_date = fields.Date('Packaging Date', readonly=True)
    sending_date = fields.Date('Sending Date', readonly=True)
    
    order_month = fields.Char('Month Order', readonly=True)
    order_quarter = fields.Char('Quarter Order', readonly=True)
    sending_month = fields.Char('Month Sending', readonly=True)
    sending_quarter = fields.Char('Quarter Sending', readonly=True)
    
    invoice_status =  fields.Char('Invoice Status', readonly=True)
    #effective_date = fields.Datetime('Effective Date', readonly=True)
    #invoice_status = fields.Selection([
    #    ('upselling', 'Upselling Opportunity'),
    #    ('invoiced', 'Fully Invoiced'),
    #    ('to invoice', 'To Invoice'),
    #    ('no', 'Nothing to Invoice')
    #    ], string='Invoice Status', readonly=True)
    price_weight = fields.Float(string='Price Weight', group_operator='avg', readonly=True)
    
    stat_prod_1 = fields.Char('statistics product 1', readonly=True)
    stat_prod_2 = fields.Char('statistics product 2', readonly=True)
    stat_prod_3 = fields.Char('statistics product 3', readonly=True)
    stat_prod_4 = fields.Char('statistics product 4', readonly=True)
    stat_prod_5 = fields.Char('statistics product 5', readonly=True)
    stat_partner_1 = fields.Char('statistics partner 1', readonly=True)
    stat_partner_2 = fields.Char('statistics partner 2', readonly=True)
    stat_partner_3 = fields.Char('statistics partner 3', readonly=True)
    stat_partner_4 = fields.Char('statistics partner 4', readonly=True)
    stat_partner_5 = fields.Char('statistics partner 5', readonly=True)
    
    fishing_type_name = fields.Char('Type of Fishing', readonly=True)
    fishing_area_name = fields.Char('Area Fishing', readonly=True)
    fishing_sub_area_name = fields.Char('Sub Area Fishing', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['invoice_status'] = ', s.invoice_status as invoice_status'
       
        fields['carrier_name'] = ', dc.name as carrier_name'
        fields['category_name'] = ', pc.complete_name as category_name'
        fields['caliber_name'] = ', hfc.name as caliber_name'
        fields['packaging_name'] = ', hfp.name as packaging_name'
        fields['sending_date'] = ', s.di_sending_date as sending_date'
        fields['packaging_date'] = ', s.di_packaging_date as packaging_date'
        
        fields['order_month'] = """, concat('M' , to_char(s.date_order, 'MM')) as order_month"""
        fields['order_quarter'] = """, concat('T0' , to_char(s.date_order, 'Q')) as order_quarter"""
        fields['sending_month'] = """, concat('M' , to_char(s.di_sending_date, 'MM')) as sending_month"""
        fields['sending_quarter'] = """, concat('T0' , to_char(s.di_sending_date, 'Q')) as sending_quarter"""
        
        fields['price_weight'] = ', avg(l.di_price_weight) as price_weight'
        fields['stat_prod_1'] = ', t.di_statistics_alpha_1 as stat_prod_1'
        fields['stat_prod_2'] = ', t.di_statistics_alpha_2 as stat_prod_2'
        fields['stat_prod_3'] = ', t.di_statistics_alpha_3 as stat_prod_3'
        fields['stat_prod_4'] = ', t.di_statistics_alpha_4 as stat_prod_4'
        fields['stat_prod_5'] = ', t.di_statistics_alpha_5 as stat_prod_5'
        fields['stat_partner_1'] = ',  partner.di_statistics_alpha_1 as stat_partner_1'
        fields['stat_partner_2'] = ',  partner.di_statistics_alpha_2 as stat_partner_2'
        fields['stat_partner_3'] = ',  partner.di_statistics_alpha_3 as stat_partner_3'
        fields['stat_partner_4'] = ',  partner.di_statistics_alpha_4 as stat_partner_4'
        fields['stat_partner_5'] = ',  partner.di_statistics_alpha_5 as stat_partner_5'
        
        fields['fishing_type_name'] = ', di_fishing_type.name as fishing_type_name'
        fields['fishing_area_name'] = ', di_fishing_area.name as fishing_area_name'
        fields['fishing_sub_area_name'] = ', di_fishing_sub_area.name as fishing_sub_area_name'
        
        from_clause += """left join delivery_carrier dc on (s.carrier_id = dc.id)
                    left join product_category pc on (t.categ_id = pc.id)
                    left join di_multi_table hfc on (t.di_caliber_id = hfc.id)
                    left join di_multi_table hfp on (t.di_packaging_id = hfp.id)
                    left join di_fishing_type on (l.di_fishing_type_id = di_fishing_type.id)
                    left join di_fishing_area on (l.di_fishing_area_id = di_fishing_area.id)
                    left join di_fishing_sub_area on (l.di_fishing_sub_area_id = di_fishing_sub_area.id)"""
       
        groupby += """, dc.name,
                    pc.complete_name, hfc.name,hfp.name,
                    s.di_sending_date, s.di_packaging_date, s.invoice_status
                    ,t.di_statistics_alpha_1, t.di_statistics_alpha_2, t.di_statistics_alpha_3, 
                    t.di_statistics_alpha_4, t.di_statistics_alpha_5, 
                    partner.di_statistics_alpha_1, partner.di_statistics_alpha_2, partner.di_statistics_alpha_3, 
                    partner.di_statistics_alpha_4, partner.di_statistics_alpha_5, di_fishing_type.name, di_fishing_area.name, di_fishing_sub_area.name

                    """
        
        return super(HubiSaleReport, self)._query(with_clause, fields, groupby, from_clause)

    def _select(self):
        return super(HubiSaleReport, self)._select() + """,dc.name as carrier_name,
                pc.complete_name as category_name, 
                
                s.di_sending_date as sending_date, s.di_packaging_date as packaging_date,
                s.invoice_status as invoice_status, avg(l.di_price_weight) as price_weight
                
                ,t.di_statistics_alpha_1 as stat_prod_1, t.di_statistics_alpha_2 as stat_prod_2
                ,t.di_statistics_alpha_3 as stat_prod_3, t.di_statistics_alpha_4 as stat_prod_4,
                t.di_statistics_alpha_5 as stat_prod_5, partner.di_statistics_alpha_1 as stat_partner_1,
                partner.di_statistics_alpha_2 as stat_partner_2, partner.di_statistics_alpha_3 as stat_partner_3,
                partner.di_statistics_alpha_4 as stat_partner_4, partner.di_statistics_alpha_5 as stat_partner_5
                """
            #s.effective_date as effective_date, 
                
    def _from(self):
        return super(HubiSaleReport, self)._from() + """left join delivery_carrier dc on (s.carrier_id = dc.id)
                    left join product_category pc on (t.categ_id = pc.id)
                    left join di_multi_table hfc on (t.caliber_id = hfc.id)
                    left join di_multi_table hfp on (t.packaging_id = hfp.id)"""

    def _group_by(self):
        return super(HubiSaleReport, self)._group_by() + """, dc.name,
                    pc.complete_name,
                    
                    s.di_sending_date, s.di_packaging_date, s.invoice_status
                    
                    ,t.di_statistics_alpha_1, t.di_statistics_alpha_2, t.di_statistics_alpha_3, 
                    t.di_statistics_alpha_4, t.di_statistics_alpha_5, 
                    partner.di_statistics_alpha_1, partner.di_statistics_alpha_2, partner.di_statistics_alpha_3, 
                    partner.di_statistics_alpha_4, partner.di_statistics_alpha_5

                    """
            #s.effective_date,        
