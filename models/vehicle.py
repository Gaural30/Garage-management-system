from odoo import models, fields, api

class GarageVehicle(models.Model):
    _name ='garage.vehicle'
    _description = 'Garage Vehicle'


    name = fields.Char(string='Vehicle Name', required=True, help="This is name of vehicle")
    registration_number = fields.Char(string='Registration Number', required=True, help = "This is number plate of Vehicle" ,size=7)
    vin_number = fields.Char(string='VIN Number', help="Unique 17-character alphanumeric code" , size=17)
    manufacturer = fields.Char(string='Manufacturer',help="Name of company")
    model = fields.Char(string='Model', help="Model of vehicle")
    year = fields.Integer(string='Year' , help="Manufacturing Year")
    km = fields.Float(string="Kilometers", help="Current Kilometers", digits=(7, 3))
    date=fields.Date(string="Date", default=fields.Date.today(), help="Today's Date" , index=True)
    time = fields.Datetime(string="DateTime", default=fields.Datetime.now(), help="Current Date and Time")
    service_type = fields.Selection(selection=[('free','Free'),('paid','Paid')], string='Srevice Type', help="Service type")
    # gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    description = fields.Text(string="Description", help="Descriptin")
    active = fields.Boolean(string='Active', default=True,invisible=True)