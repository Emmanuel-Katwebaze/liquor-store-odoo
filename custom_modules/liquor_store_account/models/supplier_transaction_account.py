from odoo import models

class SupplierTransactionAccount(models.Model):
    _inherit = 'liquor_store.supplier_transaction'
    
    def action_pending(self):
        # create an empty account.move
        move = self.env['account.move'].create({
            'partner_id': self.supplier.id,
            'move_type': 'out_invoice'
        })
        
        # Add invoice lines
        move.write({
            'invoice_line_ids': [
                (0, 0, {
                    'name': 'Transaction Price',
                    'quantity': self.amount,
                    'price_unit': self.unit_price * self.amount
                })
            ]
        })
        
        return super().action_pending()
    
