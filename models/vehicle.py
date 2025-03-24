from odoo import models, fields, api

class GarageVehicle(models.Model):
    _name ='garage.vehicle'
    _description = 'Garage Vehicle'


    name = fields.Char(string='Vehicle Name', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    registration_number = fields.Char(string='Registration Number', required=True)
    vin_number = fields.Char(string='VIN Number')
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
    year = fields.Integer(string='Year')
    last_service_date = fields.Date(string='Last Service Date')
    next_service_date = fields.Date(string='Next Service Due', default=fields.Date.today)
    service_history = fields.One2many('garage.service', 'vehicle_id', string='Service History')
    active = fields.Boolean(string='Active', default=True)