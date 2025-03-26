from odoo import models, fields, api

class GarageVehicle(models.Model):
    _name ='garage.vehicle'
    _description = 'Garage Vehicle'

    customer_id=fields.Many2one('garage.customer', "Customer" , ondelete="restrict")
    phone = fields.Char(related="customer_id.phone", string='Mobile Number')
    email = fields.Char(related="customer_id.email", string="Email")
    name = fields.Char(string='Vehicle Name', required=True, help="This is name of vehicle")
    registration_number = fields.Char(string='Registration Number', required=True, help = "This is number plate of Vehicle" ,size=10)
    vin_number = fields.Char(string='VIN Number', help="Unique 17-character alphanumeric code" , size=17)
    manufacturer = fields.Char(string='Manufacturer',help="Name of company")
    model = fields.Char(string='Model', help="Model of vehicle")
    year = fields.Integer(string='Year' , help="Manufacturing Year")
    km = fields.Float(string="Kilometers", help="Current Kilometers", digits=(7, 3))
    date=fields.Date(string="Date", default=fields.Date.today(), help="Today's Date" , index=True)
    time = fields.Datetime(string="DateTime", default=fields.Datetime.now(), help="Current Date and Time")
    service_type = fields.Selection(selection=[('free','Free'),('paid','Paid')], string='Srevice Type', help="Service type")
    
    description = fields.Text(string="Description", help="Descriptin")
    active = fields.Boolean(string='Active', default=True)
    priority = fields.Selection([(str(ele),str(ele)) for ele in range(0,5)], 'Priority')

    # password = fields.Char('Password')
    #
    # website = fields.Char("Website")

    symptom_ids = fields.One2many("garage.symptom", "vehicle_id", string="Symptoms")
    currency_id = fields.Many2one('res.currency', 'Currency')
    amount = fields.Monetary(currency_field='currency_id',string='Amount', aggregator='max')
    record_reference = fields.Reference(
        selection=[
            ('garage.customer', 'Customer'),
            ('res.partner', 'Partner'),
        ],
        string="Related Record",
        help="Select a record from multiple models"
    )
    attachment = fields.Binary(string="File Attachment", help="Upload a file")
    attachment_name = fields.Char(string="File Name", help="Preserve the file name")

    photo = fields.Image('Photo')
    repair_hours = fields.Integer(string="Repair Hours", help="Total repair time in hours")

    state = fields.Selection([
        ('received', 'Received'),
        ('diagnosed', 'Diagnosed'),
        ('in_progress', 'In Progress'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered')
    ], string="Status", default='received', tracking=True)