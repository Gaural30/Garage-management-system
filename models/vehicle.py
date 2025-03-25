from odoo import models, fields, api

class GarageVehicle(models.Model):
    _name ='garage.vehicle'
    _description = 'Garage Vehicle'


    name = fields.Char(string='Vehicle Name', required=True)
    registration_number = fields.Char(string='Registration Number', required=True)
    vin_number = fields.Char(string='VIN Number')
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
    year = fields.Integer(string='Year')
    km = fields.Float(string="Kilometers")
    date=fields.Date(string="Date", default=fields.Date.today())
    time = fields.Datetime(string="DateTime", default=fields.Datetime.now())
    service_type = fields.Selection(selection=[('free','Free'),('paid','Paid')], string='Srevice Type')
    # gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    description = fields.Text(string="Description")
    active = fields.Boolean(string='Active', default=True)