# See LICENSE file for full copyright and licensing details.

from odoo import  api, fields, models, _
import logging
_logger = logging.getLogger(__name__)

class DiDueResPartner(models.Model):
    _inherit = 'res.partner'

    
    di_total_due = fields.Float(compute='_compute_total_due', string='Total Due')
    di_total_overdue = fields.Float(compute='_compute_total_due', string='Total Overdue')
    
    #di_residual_aml_ids = fields.One2many('account.move.line', 'partner_id',
    #                                       domain=[
    #                                               ('move_id.payment_state', 'in', ('not_paid', 'partial')),
    #                                               ('move_id.state', '=', 'posted' )])
    

    def _compute_total_due(self):
        """
        Compute the fields 'total_due', 'total_overdue'
        """
        
        today = fields.Date.context_today(self)
        _logger.info("Today : %s", today)
        for record in self:
            total_due = 0
            total_overdue = 0
            
            amount_dues = self.env['account.move.line'].search([('move_id.partner_id', '=', record.id), ('move_id.move_type', 'in', ('out_invoice','in_invoice','out_refund','in_refund')), ('move_id.payment_state', 'in', ('not_paid', 'partial')), ('move_id.state', '=', 'posted' )])
            #for aml in record.di_residual_aml_ids:
            for aml in amount_dues:
                if aml.company_id == self.env.company and not aml.blocked:
                    amount = aml.amount_residual
                    total_due += amount
                    _logger.info("Total du : %s", total_due)
                    is_overdue = today > aml.date_maturity if aml.date_maturity else today > aml.date
                    if is_overdue and not aml.blocked:
                        total_overdue += amount
                        _logger.info("Total overdu : %s", total_overdue)
            record.di_total_due = total_due
            record.di_total_overdue = total_overdue
    def action_view_amount_due(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("account.action_move_out_invoice_type")
        action['domain'] = [
            ('move_type', 'in', ('out_invoice', 'out_refund')),
            ('partner_id', 'child_of', self.id),
        ]
        action['context'] = {'default_move_type':'out_invoice', 'move_type':'out_invoice', 'journal_type': 'sale', 'search_default_open': 1}
        return action


    
        
