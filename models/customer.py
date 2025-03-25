from odoo import models, fields

class Customer(models.Model):
    _name= 'garage.customer'
    _description = 'Customers'


    name = fields.Char(string="Name")
    phone = fields.Char(string="Mobile Number")
    email = fields.Char(string="Email")






