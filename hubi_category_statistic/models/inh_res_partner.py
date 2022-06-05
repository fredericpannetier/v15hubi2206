# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class HubiCatStatResPartner(models.Model):
    _inherit = "res.partner"
    
    def write(self, vals):
        _logger.info("write")
        result = super(HubiCatStatResPartner, self).write(vals)
        _write_categ_partner = self.env['ir.config_parameter'].sudo().get_param('hubi.di_write_categ_partner')
        if _write_categ_partner:
            for record in self:
                categ_ids = record.category_id
                _logger.info("Listes des catégories : %s", categ_ids)
                i = -1
                for categ in categ_ids:
                    parent_categ=categ.parent_path
                    list_parent_categ = parent_categ.split("/")
                    _logger.info("Listes des parents : %s", list_parent_categ)
                    for parent_categ in list_parent_categ:
                        if parent_categ:
                            categ = self.env['res.partner.category'].search([('id', '=ilike', parent_categ)], limit=1)
                            if categ.name:
                                _logger.info("i = %s - Code catégorie : %s - Nom catégorie : %s", i,parent_categ,categ.name)
                                i+=1
                                if i == 0:
                                    vals['di_statistics_alpha_1'] = categ.name
                                elif i == 1:
                                    vals['di_statistics_alpha_2'] = categ.name
                                elif i == 2:
                                    vals['di_statistics_alpha_3'] = categ.name
                                elif i == 3:
                                    vals['di_statistics_alpha_4'] = categ.name
                                elif i == 4:
                                    vals['di_statistics_alpha_5'] = categ.name
                                
                
            _logger.info("Listes des valeurs modifiées : %s", vals)            
            result = super(HubiCatStatResPartner, self).write(vals) 