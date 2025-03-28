from odoo import fields, models

class JobCard(models.Model):
    _name="garage.jobcard"
    _description = "This is for make a job card for Vehicles"
    _rec_name = "customer_id"


    customer_id= fields.Many2one("garage.vehicle" , string="Customer Name" , required=True)
    vehicle_name = fields.Char(related="customer_id.vehicle_name" , string="Vehicle Name")
    registration_number=fields.Char(related="customer_id.registration_number", string="Registration Number")
    vehicle_model = fields.Char(related="customer_id.vehicle_model", string="Model")
    service_type = fields.Selection(selection=[('free',"Free"),('paid','Paid')], string="Service type")
    mechanic_id = fields.Many2one('hr.employee', string="Mechanic")
    symptom_ids = fields.One2many("garage.repair", "jobcard_id", string="Symptoms")
    service_date= fields.Date(string="Date" ,default=fields.Date.today())
    description = fields.Text(string="Description", help="If proble is not i Symptom")