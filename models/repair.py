from odoo import models, fields


class repair(models.Model):
    _name="garage.repair"
    _description = "This is for add one2many in vehiches"


    repair_id = fields.Many2one("garage.vehicle", "Vehicle")

    name=fields.Many2one("garage.symptom","symptom")