from odoo import models, fields ,api


class SpareParts(models.Model):
    _name="garage.sparepart"
    _description="Garage Spare part Inventry"

    
    name = fields.Char(string="Part Name", required=True)
    # part_number = fields.Char(string="Part Number", required=True, unique=True)
    product_id = fields.Many2one('product.product', string="Linked Product", required=True)
    product_id = fields.Many2one('product.product', string="Linked Product", required=True)  # Link to Inventory
    quantity = fields.Float(related='product_id.qty_available', string="Stock Quantity", readonly=True)
    cost_price = fields.Float(related='product_id.standard_price', string="Cost Price", readonly=True)
    sale_price = fields.Float(related='product_id.list_price', string="Sale Price", readonly=True)
    location_id = fields.Many2one('stock.location', string="Stock Location")


    
    