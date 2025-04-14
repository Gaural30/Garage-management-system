# from odoo import fields, models ,api

# class JobCard(models.Model):
#     _name="garage.jobcard"
#     _description = "This is for make a job card for Vehicles"
#     _rec_name = "customer_id"


#     customer_id= fields.Many2one("garage.vehicle" , string="Customer Name" , required=True)
#     vehicle_name = fields.Char(related="customer_id.vehicle_name" , string="Vehicle Name")
#     registration_number=fields.Char(related="customer_id.registration_number", string="Registration Number")
#     vehicle_model = fields.Char(related="customer_id.vehicle_model", string="Model")
#     service_type = fields.Selection(selection=[('free',"Free"),('paid','Paid')], string="Service type")
#     mechanic_id = fields.Many2one('hr.employee', string="Mechanic")
#     symptom_ids = fields.One2many("garage.repair", "jobcard_id", string="Symptoms")
#     service_date= fields.Date(string="Date" ,default=fields.Date.today())
#     description = fields.Text(string="Description", help="If proble is not i Symptom")
#     spare_part_ids = fields.Many2many('garage.sparepart', string="Spare Parts Used")


from odoo import fields, models, api

class JobCard(models.Model):
    _name = "garage.jobcard"
    _description = "This is for making a job card for Vehicles"
    _rec_name = "customer_id"

    customer_id = fields.Many2one("garage.vehicle", string="Customer Name", required=True)
    vehicle_name = fields.Char(related="customer_id.vehicle_name", string="Vehicle Name")
    registration_number = fields.Char(related="customer_id.registration_number", string="Registration Number")
    vehicle_model = fields.Char(related="customer_id.vehicle_model", string="Model")
    service_type = fields.Selection(selection=[('free', "Free"), ('paid', 'Paid')], string="Service type")
    mechanic_id = fields.Many2one('hr.employee', string="Mechanic")
    symptom_ids = fields.One2many("garage.repair", "jobcard_id", string="Symptoms")
    service_date = fields.Date(string="Date", default=fields.Date.today())
    description = fields.Text(string="Description", help="If problem is not in Symptoms")
    spare_part_ids = fields.Many2many('garage.sparepart', string="Spare Parts Used")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ], default='draft', string='State')

    # @api.model
    # def create(self, vals):
    #     job_card = super(JobCard, self).create(vals)
    #     job_card._update_spare_parts_stock()
    #     return job_card

    # def write(self, vals):
    #     res = super(JobCard, self).write(vals)
    #     if 'spare_part_ids' in vals:
    #         self._update_spare_parts_stock()
    #     return res

    # def _update_spare_parts_stock(self):
    #     """ Reduce the On-Hand Quantity of spare parts when added to the Job Card. """
    #     for spare_part in self.spare_part_ids:
    #         if spare_part.product_id and spare_part.product_id.type == 'product':
    #             if spare_part.product_id.qty_available > 0:
    #                 spare_part.product_id.qty_available -= 1
    #             else:
    #                 raise models.ValidationError(
    #                     f"Not enough stock for {spare_part.name}. Please restock before using."
    #                 )
