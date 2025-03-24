from odoo import models, fields

class GarageService(models.Model):
    _name = 'garage.service'
    _description = 'Garage Service'

    vehicle_id = fields.Many2one('garage.vehicle', string='Vehicle', required=True)
    date = fields.Date(string='Service Date', default=fields.Date.today)
    service_type = fields.Selection([
        ('oil_change', 'Oil Change'),
        ('tire_change', 'Tire Change'),
        ('brake_service', 'Brake Service'),
        ('engine_repair', 'Engine Repair'),
        ('diagnostics', 'Diagnostics'),
        ('other', 'Other')
    ], string='Service Type', required=True)
    cost = fields.Float(string='Cost', digits=(6, 2))
    mechanic_id = fields.Many2one('hr.employee', string='Mechanic')
    notes = fields.Text(string='Service Notes')
