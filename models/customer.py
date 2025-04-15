from odoo import models, fields, api

class Customer(models.Model):
    _name= 'garage.customer'
    _description = 'Customers'


    name = fields.Char(string="Name")
    # numeric = fields.Inte
    phone = fields.Char(string="Mobile Number")
    cust_id = fields.Integer(string="Customer ID")
    email = fields.Char(string="Email", copy=False)
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
        string='Customer Symptoms',
        copy= True
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
         """
        Fetch the values of normal and relational fields from a recordset.
        --------------------------------------------------------------
        @param self: object pointer
         """
         res= self.browse(4)
         print(res.name)
         print(res.phone)
         relational_field = res.symp_idss
         for i in relational_field:
              print("relationla field",i.name)
        

    def multiple_recordset(self):
         """ 
         Try to fetch the fields from a multiple record recordset.
          --------------------------------------------------------------
        @param self: object pointer
         """

         res = self.env['garage.vehicle.company'].search([])
         for i in res:
              print(i.company_name)
    
    def ensure_one_method(self):
         """
         Fetch the predefined fields / magic fields for a record from a
         recordset containing a single record.
         Fetch the predefined fields / magic fields for multiple records
         from a recordset containing multiple records.
         --------------------------------------------------------------
        @param self: object pointer
         """
         rec = self.browse(26)
         rec.ensure_one()
         print("Name: ",rec.name)
         print("ID:", rec.id)
         print("Created On:", rec.create_date)
         print("Last Updated On:", rec.write_date)
         print("Created By:", rec.create_uid.name)
         print("Last Updated By:", rec.write_uid.name)
         print("Display Name:", rec.display_name)
         # It will raise an error if there are multiple records in the recordset.

         partners = self.env['garage.vehicle.company'].search([])
         for partner in partners:
            print("ID:", partner.id)
            print("Created on:", partner.create_date)
            print("Created by:", partner.create_uid.name)
            print("Last Updated:", partner.write_date)
            print("Updated by:", partner.write_uid.name)

    def filter_val(self):
        #  ids_without_email = self.search([('email', '=', False)])
        #  print("ID without email",ids_without_email)

        all_records = self.search([])  
        ids_without_email = all_records.filtered(lambda rec: not rec.email)
        print("IDs without email:", ids_without_email)


        ids_with_email = all_records.filtered(lambda rec: rec.email)  
        print("IDs with email:", ids_with_email)


        filtered_records_without_lambda = self.search([
        ('email', '!=', False), 
        ('manufacturer.company_name', '=', 'tatacar')])
        print("Filtered Records without lambda:", filtered_records_without_lambda)

        filtered_records = all_records.filtered(
        lambda rec: rec.email and rec.manufacturer and rec.manufacturer.company_name.lower() == 'tatacar')
        print("Filtered Records with multiple conditions:", filtered_records)

    def print_email(self):
        """
        Get the value of a field from multiple record recordset for all
        the records in a list.
        Perform the same operation as above using lambda
        --------------------------------------------------------------
        @param self: object pointer
        """
        partners = self.search([])  
        emails = partners.mapped('email')  
        print("Emails:", emails)

        emails = partners.mapped(lambda rec: rec.email)
    
        print("Emails using Lambda:", emails)

    def sort_records(self):
            """
            Sort the records in a recordset with a field.
            Perform the same operation with lambda.
            --------------------------------------------------------
            @param self: object pointer           
            """
            records = self.search([])  
            sorted_records_lambda= sorted(records, key=lambda rec: rec.name or "")
            print("Sorted Records:", [(rec.id, rec.name) for rec in sorted_records_lambda])

            without_lambda = sorted(records)
            print("Sorted Records",without_lambda)

            without_lambda_decending = records.sorted(lambda rec:rec.id,reverse=True)   
            print("Record sorted decending",without_lambda_decending) 

    def check_rec_exit(self):
         
         """
         Check whether a single record exists in a recordset containing multiple records or not.
         ---------------------------------------------------------------------------------------
         @param self: object pointer           
         """

         records = self.search([])

        
         record_to_check = self.browse(4)

            # Check if the record exists in the recordset
         if record_to_check in records:
                print(f"Record with ID {record_to_check.id} exists.")
         else:
                print(f"Record with ID {record_to_check.id} does not exist.")


    def create_record(self):
         """
         Create records from a button click in the same model
         using all types of fields.
         ----------------------------------------------------
         @param self: object pointer
         """

         new_rec = self.create({
              'name':"Jal Disuza",
              'email':'jal@gmail.com',
              'phone':'4512121245',

         })


         new_rec_another_model=self.env['garage.vehicle.company'].create({
              'company_name':'Fararri'
         })

         for rec in self:

                new_rec={'symp_ids':[(0,0,{
                    'name': 'New symptom',
                'labor_hours': '5.30', 
                'part_cost': '500',
                'service_charge':'650'
                })]}

                rec.create(new_rec)

                new_rec1 = {'symp_idss':[(4,3),(4,2),(4,1)]}
                rec.create(new_rec1)



                symptom_ids_to_link = [5, 6, 7]

                new_rec2 = {'symp_idss':[(6,0,symptom_ids_to_link)]}
                rec.create(new_rec2)
    
    
    def write_record(self):
         """
         This is for Write method in ORM
         ---------------------------------
         @param self: object pointer
         """
        #  update_rec = self.write({
        #       'name':"Piter Disuza",
        #       'email':'piter@gmail.com',
        #       'phone':'4512121245',

        #  })

        #  update_another_model=self.env['garage.vehicle.company'].search([('id', '=', 1)]).write({
        #       'company_name':'Jagure'
        #  })


         for rec in self:

# Update the O2M field and create a new record in O2M field using both 0,0 and Command.create

                # new_rec={'symp_ids':[(0,0,{
                #     'name': 'Change Wheels',
                # 'labor_hours': '2', 
                # 'part_cost': '5000',
                # 'service_charge':'7000'
                # })]}

                # rec.write(new_rec)


# Update the O2M field and update an existing record’s fields using 1,<id> 

                # update_rec={'symp_ids':[(1,10,{
                # 'name': 'update symptom',
                # 'labor_hours': '5.30', 
                # 'part_cost': '500',
                # 'service_charge':'650'
                # })]}

                # rec.write(update_rec)

# Update the O2M field and delete an existing record making sure it is deleted from the comodel’s table as well
               

                # del_reco_db_ui =  {'symp_ids':[(2,2)]}
                # rec.write(del_reco_db_ui)

# Update the O2M field and delete an existing record making sure it is not deleted from the comodel’s table as well.

                # del_rec_ui =  {'symp_ids':[(3,20)]}
                # rec.write(del_rec_ui)

# Update the O2M field and link an existing record from the comodel

                    new_rec = {'symp_ids':[(4,17),(4,18),(4,19)]}
                    rec.write(new_rec)

# Remove all the records from the O2M field.

                # rmv_all_rec = {'symp_ids': [(5,0,0)]}
                # rec.write(rmv_all_rec)

# Link new records removing the existing records in an O2M field


                # replace_rec = {'symp_ids': [(6,0,[7,8,9,11])]}
                # rec.write(replace_rec)


# Update M2M field to link a value keeping existing values as it is in the M2M field


              
                # update_rec = {'symp_idss':[(4,17),(4,18),(4,19)]}
                # rec.write(update_rec)

# Update M2M field to remove existing values and add new values


                # replace_rec = {'symp_idss':[(6,0,[3,20,27])]}
                # rec.write(replace_rec)

# Update M2M field to remove all values

                # remove_all = {'symp_idss':[(5,0,0)]}
                # rec.write(remove_all)

    def browse_record(self):


            # Browse single record
            rec5 = self.browse(30)
            print("Rec 5", rec5.name)


            # Browse Multiple Records
            # rec34 = self.browse([3,4])
            # print("Rec 3 and 4", rec34)


            # # browse form another model 
            # other_module = self.env['garage.jobcard']

            # # # Single 
            # job4 = other_module.browse(4)
            # print("Job 4", job4)


            # # # multiple
            # job56 = other_module.browse([5,6])
            # for rec in job56:
                
            #         print("job 5 and 6 ", rec.service_date)


    def read_method(self):

        # Reading all values of current record 
        # crt_rec = self.read()
        # print("Current Record", crt_rec)

        # # Reading specific value of current record 
        # spe_value = self.read(['name','phone'])
        # print("Specific values", spe_value)

        # rel_val = self.read(['birthdate','symp_idss','symp_ids','manufacturer'])
        # print("Specific values", rel_val)

        another_model = self.env['garage.jobcard']

        new = another_model.browse(4)
        print("Another model Data:-----",new.read())

    def copy_method(self):
        """
        This method will perform copy() operation
        ---------------------------------------------
        @param self: object pointer
        """


# this will make a copy of current record
        # copy_rec= self.copy()
        # print(copy_rec)


# Duplicate multiple records of the current model.

        # cp_273 = self.browse([26,4])
        # new_res = cp_273.copy()
        # print(new_res)

# Duplicate a record and make sure their O2M field is also copied. ----> copy = True in o2m Field 

# Duplicate a record and make sure two fields which were by default copied are now not copied. ---> copy = False
# added in email field 

# Duplicate a record such that you’re able to differentiate the original record and duplicate record.

        for rec in self:
            default = {
                'name': rec.name + ' (Copy)'
            }
            # default is used to update the value of the fields before creating the new record.
            new_rec = rec.copy(default=default)
            print("NEW REC", new_rec)

    def unlink_method(self):
         """
        This method will perform unlink() operation
        ---------------------------------------------
        @param self: object pointer
        """

# Delete a record from the current model.

        # unlic = self.unlink()
        # print(unlic)

# Delete multiple records from the current model.

        # unlic_multiple = self.browse([39,40,28,29])
        # rmv = unlic_multiple.unlink()
        # print("Records are remove form DB", rmv)

# Delete records of another model.

         another_rec=  self.env['garage.vehicle.company']
         rmv = another_rec.browse([6])
         rmv.unlink()


    def search_method(self):
         """
        This method will perform search() operation
        ---------------------------------------------
        @param self: object pointer
        """
         
# Fetch all the records from the current model.
         
        #  all_rec = self.search([])
        #  print("Search",all_rec)

# Fetch specific records from the current model.

        #  specific_rec = self.search([('manufacturer', '=','tatacar')])
        #  print("Search",specific_rec)
# Fetch specific records from another model.
        
        #  another_rec=  self.env['garage.vehicle.company']
        #  specific_rec = another_rec.search([('company_name', '=','tatacar')])
        #  print(specific_rec)

# Fetch maximum 5 records.
        #  five_limit_rec = self.search([],limit=5)
        #  for i in five_limit_rec:
        #         print("Search name=",i.name)
        #  print(five_limit_rec)


# Fetch the records specifically skipping the initial few records.
         five_offset_rec = self.search([],offset=5)
         for i in five_offset_rec:
                print(i.name)
         print(five_offset_rec)


# Fetch the records sorted by name.

        #  sorted_by_name = self.search([],order='name')
        #  for i in sorted_by_name:
        #       print(i.name)
        #  print("ASCENDING", sorted_by_name)

# Fetch the records sorted by date in a descending order.

        #  sorted_by_date = self.search([], order ='birthdate desc')
        #  for i in sorted_by_date:
        #       print(i.birthdate)
        #  print(sorted_by_date)

# Fetch the records using all the parameters and note down the priority given to each parameter.
       
        #  priority = self.search([],order='name', limit = 7, offset=3)
        #  for i in priority:
        #       print(i.name)
        #  print(priority)

        # priority = domain->order->offset->limit.


    def search_count_method(self):
         """
        This method will perform search_count() operation
        ---------------------------------------------
        @param self: object pointer
        """
         
# Count the no of records available in the current model

         count_rec = self.search_count([])
         print('Total Records: ', count_rec)

# Check the no of records based on a certain condition in the current model.

         specific  =self.search_count([('manufacturer', '=','TVScar')])
         
         print("Total Record which has KIA car:",specific)

# Count the no of records in another model.
         another_rec=  self.env['garage.vehicle.company']
         count_rec=another_rec.search_count([])
         print("Total Car Company:",count_rec)

    def search_read_method(self):
         """
        This method will perform search_read() operation
        ---------------------------------------------
        @param self: object pointer
         """


# Fetch all the records of the current model with all their fields in a list of dictionaries.

        #  all_fields= self.search_read()
        #  print("ALL", all_fields)

# Fetch only relational fields of specific records of the current model in a list of dictionaries.
        #  relational_fields = self.search_read(fields=['manufacturer','symp_ids','symp_idss'])
        #  print("Relational Fileds are:   ",relational_fields)


        #  if m2o is not their then it is False 
        # if m2m and o2m is not ther then it is is balnk list otherwise this is the ID of thar record
        # eg-->[{'id': 4, 'manufacturer': (11, 'Kiacar'), 'symp_ids': [17, 18, 19], 'symp_idss': [17, 18]},

# Fetch the records of another model sorted by their name in a list of dictionaries 
         another_rec=  self.env['garage.vehicle.company']

         sorted_by_name = another_rec.search_read(fields=['company_name'], order='company_name')

         print(sorted_by_name)

    def read_group_method(self):
         """
        This method will perform read_group() operation
        ---------------------------------------------
        @param self: object pointer
         """

# Call the read_group() method using the numerical fields and grouping fields like selection and many2one


        #  res = self.read_group([], fields=['gender','cust_id'], groupby=['gender'])
        #  print("Group: ", res)


# Call the read_group() method using the numerical fields and grouping fields but with multiple grouping.
        #  result = self.read_group(
        #     domain=[],
        #     fields=['gender', 'manufacturer'],
        #     groupby=['gender', 'manufacturer'],
        #     lazy=False  
        # )
        #  print(result)

# Perform the same operation as above and bring the second level grouping information as well.

        #  result = self.read_group(
        #     domain=[],
        #     fields=['gender', 'manufacturer'],
        #     groupby=['gender', 'manufacturer'],
        #     lazy=True 
        # )
        #  print(result)

# Perform the read_group() method but sort the records by the group by field.

         result = self.read_group(
            domain=[],
            fields=['gender', 'manufacturer'],
            groupby=['gender', 'manufacturer'],
            lazy=False ,
            limit = 1
        )
         print(result)


# Add a button on the form view on the page of a one2many
# field. When you click this button it will add a record in the one2many field.


    def add_o2m(self):
         """
         Add a button on the form view on the page of a one2many
         field. When you click this button it will add a record 
         in the one2many field.
         -----------------------------------------------------------
         @param self: object pointer
         """
         for i in self:
              
              new_rec = {'symp_ids':[(4,17),(4,18),(4,19)]}
              i.write(new_rec)

    def rmv_o2m(self):
         """
         Add another button on the page of one2many field when you
         click on this button it will remove all the records in one2many.
         ---------------------------------------------------------------
         @param self: object pointer
         """
         
         for i in self:
              
              rmv_rec = {'symp_ids':[(5,0,0)]}
              i.write(rmv_rec)
     

    def copy_rec(self):
         """
         Duplicate a record without using the copy method.
         -----------------------------------------------------
         @param self: object pointer
         """
         for i in self:
             copy_rec ={'name':i.name+'(copy)', 'email': i.email, 'phone': i.phone}
             i.create(copy_rec)
             print("COPY REC")

    def male_list(self):
         """
         Get a list of dictionaries for all the male records from your
         model (or use any other condition) without using the
         search_read() method.
         -------------------------------------------------------------
         @param self: object pointer
         """
         all_recs = self.search([('gender','=','male')])
         print("SEARCH",all_recs)
         res_recs = all_recs.read()
         print('ALL RECORDS', res_recs)

    def creater(self):
         """
         Get a recordset of the user who created the record.
         --------------------------------------------------
         @param self: object pointer
         """
         print("Recordser of Current User", self.env.user)

    def update_name_with_user(self):
        """
        Add a button when clicked will update the user_id field with
        the current logged in user.
        ------------------------------------------------------------
        @param self: object pointer
        """
        for i in self:
            i.name = self.env.user.name