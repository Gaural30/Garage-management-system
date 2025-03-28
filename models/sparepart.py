from odoo import models, fields ,api


class SpareParts(models.Model):
    _name="garage.sparepart"
    _description="Garage Spare part Inventry"

    
    name = fields.Char(string="Part Name", required=True)
    part_number = fields.Char(string="Part Number", required=True, unique=True)
    quantity = fields.Integer(string="Stock Quantity", default=0)
    cost_price = fields.Float(string="Cost Price", digits=(6,2))
    sale_price = fields.Float(string="Sale Price", digits=(6,2))
    supplier_id = fields.Many2one('res.partner', string="Supplier")
    location_id = fields.Many2one('stock.location', string="Stock Location")


    
    @api.depends('qty_available')
    def _compute_stock(self):
        """ Updates stock quantity dynamically from inventory """
        for record in self:
            record.quantity = record.qty_available