# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning, UserError, AccessError
import logging

_logger = logging.getLogger(__name__)

class HubiCatStatProductTemplate(models.Model):
    _inherit = "product.template"
    

    def write(self, vals):
        result = super(HubiCatStatProductTemplate, self).write(vals)
        _write_categ_product = self.env['ir.config_parameter'].sudo().get_param('hubi.di_write_categ_product')
        if _write_categ_product:
            for record in self:
                Nom_Categ=record.categ_id.complete_name
                Nom_Categ = Nom_Categ.split("/")
                i = 0
                for categ in Nom_Categ:
                    if Nom_Categ[i]:
                        if i == 0:
                            vals['di_statistics_alpha_1'] = categ
                        elif i == 1:
                            vals['di_statistics_alpha_2'] = categ
                        elif i == 2:
                            vals['di_statistics_alpha_3'] = categ
                        elif i == 3:
                            vals['di_statistics_alpha_4'] = categ
                        elif i == 4:
                            vals['di_statistics_alpha_5'] = categ
                    i+=1
            result = super(HubiCatStatProductTemplate, self).write(vals)    
    