from odoo import models, fields, api

class Customer(models.Model):
    _name= 'garage.customer'
    _description = 'Customers'


    name = fields.Char(string="Name")
    phone = fields.Char(string="Mobile Number")
    cust_id = fields.Integer(string="Customer ID")
    email = fields.Char(string="Email")
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    birthdate = fields.Date('Birthdate', default=fields.Date.today())
    manufacturer = fields.Many2one("garage.vehicle.company",help="Name of company", string='Manufacturer')
    model = fields.Char(string="Model")
    active = fields.Boolean('Active', default=True)
    # manufacturer = fields.Many2one("garage.vehicle.company",help="Name of company", string='Manufacturer',domain=[('company_name','ilike','car')])

    # symp = fields.Many2Many(comodel_name='garage.symptom', relation="cust_symp", )
    # symp_idss = fields.Many2many(
    #     comodel_name='garage.symptom',
    #     relation='garage_customer_symptom_rel',
    #     column1='customer_id',
    #     column2='symptom_id',
    #     string="Symptoms",
    #     domain=[('name','ilike','change')]
    # )
    symp_idss = fields.Many2many(
        comodel_name='garage.symptom',
        relation='garage_customer_symptom_rel',
        column1='customer_id',
        column2='symptom_id',
        string="Symptoms",
        
    )

    symp_ids = fields.One2many(
        comodel_name='garage.symptom',
        inverse_name='customer_id',
        string='Customer Symptoms'
    )


    symptom_count = fields.Integer(string="Symptoms", compute="_compute_symptom_count")

    # user_id = fields.Many2one('garage.vehicle.company', 'Company name', default=lambda self: self.env.uid)
    user_id = fields.Many2one('res.users', 'User', default=lambda self: self.env.user.id)
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company.id
    )

    def _compute_symptom_count(self):
        for record in self:
            count = self.env['garage.symptom'].search_count([('customer_id', '=', record.id)])
            record.symptom_count = count


    def action_view_symptoms(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Symptoms',
            'view_mode': 'list,form',
            'res_model': 'garage.symptom',
            'domain': [('customer_id', '=', self.id)],
            'context': {'default_customer_id': self.id}
        }

    def record_name(self):
         print(self.name)

  


        
    # this will create only customer 
    def create_sample_customer_only(self):
    


        #  for 0,0 (create) (O2M)
        # for rec in self:

        #     new_rec={'symp_ids':[(0,0,{
        #         'name': 'New symptom',
        #     'labor_hours': '5.30', 
        #     'part_cost': '500',
        #     'service_charge':'650'
        #     })]}

        #     rec.write(new_rec)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       #  for 1,id (update) (O2M)
    #    for rec in self:

    #         new_rec={'symp_ids':[(1,14,{
    #             'name': 'New symptom again',
    #         'labor_hours': '5.30', 
    #         'part_cost': '500',
    #         'service_charge':'650'
    #         })]}

    #         rec.write(new_rec)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      
        # for 2,id (delete) (O2M)

        # for rec in self:
        #     new_rec =  {'symp_ids':[(2,14)]}
        #     rec.write(new_rec)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # for 3,id (unlink) (O2M)
        # for rec in self:
        #     new_rec =  {'symp_ids':[(3,10)]}
        #     rec.write(new_rec)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # for [(4,id)] M2M
        # for rec in self:
        #     new_rec = {'symp_idss':[(4,3),(4,2),(4,1)]}
        #     rec.write(new_rec)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # for [(6,0,[id,id])] M2M


        # for rec in self:
        #     new_rec = {'symp_idss':[(6,0,[5])]}
        #     rec.write(new_rec)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        for rec in self:
            new_rec = {'symp_idss':[(5,0,0)]}
            rec.write(new_rec)


    def browse_record(self):

        # Browse single record
        rec5 = self.browse(25)
        # id5 = rec5.name
        print("Rec 5", rec5.name)


        # Browse Multiple Records
        # rec34 = self.browse([3,4])
        # print("Rec 3 and 4", rec34)


        # browse form another model 
        other_module = self.env['garage.jobcard']

        # Single 
        job4 = other_module.browse(4)
        print("Job 4", job4)


        # multiple
        job56 = other_module.browse([5,6])
        for rec in job56:
            
                print("job 5 and 6 ", rec.service_date)



    def read_method(self):

        # Reading all values of current record 
        crt_rec = self.read()
        print("Current Record", crt_rec)

        # Reading specific value of current record 
        spe_value = self.read(['name','phone'])
        print("Specific values", spe_value)

    def copy_method(self):


        # this will make a copy of current record
        copy_rec= self.copy()
        print(copy_rec)

    def unlink_method(self):

        unlic = self.unlink()
        print(unlic)

    def search_method(self):
         all_rec = self.search([])
         print("Search",all_rec)

         all_limit_rec = self.search([],limit=3)
         for i in all_limit_rec:
                print("Search name=",i.name)
         print(all_limit_rec)

         offset_rec = self.search([],offset=3)
         for i in offset_rec:
              print("name = ",i.name)
         print("offset = ", offset_rec)

         all_rec_other = self.env['garage.jobcard'] 
         all_rec1=all_rec_other.search([],limit=5,order="vehicle_name desc")
         for i in all_rec1:
              print("name",i.vehicle_name)

    def forEnv(self):
         print("Environment is ",self.env) 
    
    def Cursor(self):
        
         print("Cusror", self.env.cr)

         self.env.cr.execute('select name, id from garage_customer')

         res = self.env.cr.fetchone()
         print("RESULT", res)

         res1 = self.env.cr.fetchall()
         print("ALL Result", res1)

         self.env.cr.execute('select name, id from garage_customer')
         res2 = self.env.cr.dictfetchone()
         print("Dictionary Formate ", res2)

         res3=self.env.cr.dictfetchall()
         print("Dictionary formate All", res3)

         self.env.cr.execute("update garage_customer set name= 'Khushali Patel' where id = 30")

         self.env.cr.execute("delete from garage_customer where id=31")    

    def crt_login_user(self):
         print("Current User",self.env.uid)
         print("Recordser of Current User", self.env.user)
         print("Company of Current User", self.env.company)
         print("Companies of Current User", self.env.companies)
         print("Language  of Current User", self.env.lang)
         print("Context of Current User", self.env.context)

    def another_model(self):
        #  an = self.env['garage.jobcard']  




         print("Object of Another Model:- ",self.env['garage.jobcard'])


        #  22
         mykey = list(self.env.keys())
         print("KEYS", mykey)
        # 23
         val = list(self.env.values())
         print("Values", val)
        # 24
         itm = list(self.env.items())
         print("items", itm)

    def xml_id(self):
        view = self.env.ref('gsm.view_customer_form')
        print(view)
        action = self.env.ref('gsm.action_garage_customer')
        print(action)
        menu = self.env.ref('gsm.garage_customer_male')
        print(menu)
        group = self.env.ref('gsm.grp_garage_admin')
        print(group)
        access = self.env.ref('gsm.access_customer_admin')
        print(access)
        admin = self.env.ref('base.user_admin')
        print(admin)
        company = self.env.ref('base.main_company')
        print(company)


# what is self: self refers to the current recordset

    def blank_recordset(self):
         empty_recordset = self.env['garage.jobcard'].browse([])
         print("Blank Recordset",empty_recordset)

    def iterate(self):
         """
        Iterate in a recordset to fetch a single record recordset.
        --------------------------------------------------------------
        @param self: object pointer
        """
         iterte_rec = self.env['garage.vehicle.company'].search([])
         for i in iterte_rec:
              print(i.company_name)
              
    def normal_field(self):
         res= self.browse([4])
         print(res.name)
         print(res.phone)

