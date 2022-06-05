# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class HubidiFishingType(models.Model):
    _name = "di.fishing.type"
    _description = "Type of Fishing"
    
    name = fields.Char(string = "Name", required = True, translate=True)
    
class HubidiFishingArea(models.Model):
    _name = "di.fishing.area"
    _descripion = "Area Fishing"
    
    name = fields.Char(string = "Name", required = True, translate=True)
    sub_area_ids = fields.One2many('di.fishing.sub.area','area_id', 'Sub Area Fishing')

class HubidiFishingSubArea(models.Model):
    _name = "di.fishing.sub.area"
    _description = "Sub Area Fishing"
    
    name = fields.Char(string = "Name", required = True, translate=True)
    area_id = fields.Many2one('di.fishing.area', string="Area Fishing", required = True)