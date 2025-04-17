from odoo import fields, models


class VehicleCompany(models.Model):
    _name="garage.vehicle.company"
    _description="Vehicles Company"
    _rec_name="company_name"


    company_name = fields.Char(string="Company Name")