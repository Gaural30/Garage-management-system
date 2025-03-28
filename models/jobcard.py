from odoo import fields, models ,api

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
    spare_part_ids = fields.Many2many('garage.sparepart', string="Spare Parts Used")


    @api.model
    def create(self, vals):
        """ Deducts spare part stock when job card is created """
        job_card = super(JobCard, self).create(vals)
        for spare_part in job_card.spare_part_ids:
            if spare_part.qty_available > 0:
                spare_part.qty_available -= 1  # Deducts stock
            else:
                raise ValueError(f"Not enough stock for {spare_part.name}")
        return job_card