from odoo import models, fields

class Symptom(models.Model):
    _name='garage.symptom'
    _description = "Symptoms"

    
    name=fields.Char(string="Symptom Name")
    vehicle_id = fields.Many2one("garage.vehicle", string="Vehicle")



    labor_hours = fields.Float(string="Labor Hours", help="Number of labor hours needed for repair")
    part_cost = fields.Float(string="Part Cost", help="Cost of parts required for repair")
    service_charge = fields.Float(string="Service Charge", help="General service charge")
    customer_id = fields.Many2one('garage.customer', string="Customer")
