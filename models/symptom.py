from odoo import models, fields

class Symptom(models.Model):
    _name='garage.symptom'
    _description = "Symptoms"

    
    name=fields.Char(string="Symptom Name")
    vehicle_id = fields.Many2one("garage.vehicle", string="Vehicle")