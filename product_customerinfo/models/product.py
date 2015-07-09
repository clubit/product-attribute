from openerp import models, fields

# Template taken from product.supplierinfo
class product_customerinfo(models.Model):
    _name = 'product.customerinfo'
    _description = 'Product customer information'

    name = fields.Many2one('res.partner', 'Customer', required=True, domain=[('customer', '=', True)], ondelete='cascade')
    product_id = fields.Many2one('product.template', 'Product', required=True, ondelete='cascade')
    product_name = fields.Char('Customer Product Name', help="This customer's product name will be used when creating a sales order. Keep empty to use the internal one.")
    product_code = fields.Char('Customer Product Code', size=64, help="This customer's product code will be used when creating a sales order. Keep empty to use the internal one.")

class product_template(models.Model):
    _inherit = 'product.template'

    customer_ids = fields.One2many('product.customerinfo', 'product_id', 'Customer')
