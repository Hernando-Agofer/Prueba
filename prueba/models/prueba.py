from odoo import models, fields, api


class prueba(models.Model):
    _name = 'prueba_prueba'
    _description = 'prueba_prueba'

    user = fields.Char(string='User')
    partner = fields.Char(string='Partner')
    product = fields.Char(string='Product')
    description = fields.Text(string='Activities')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
    ], string='State', defaul='draft')

    # Inherit
    partner_ids = fields.Many2one('res.partner', 'Partner')
    product_ids = fields.Many2one('product.product', 'Product')
    user_ids = fields.Many2one('res.users', 'User')

    def action_quotation(self):
        self.ensure_one()
        self.write({
            'partner': self.partner_ids.name,
            'product': self.product_ids.name,
            'user': self.user_ids.name,
            'state': 'confirm'
        })
