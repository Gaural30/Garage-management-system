{
    'name': 'Garage management system',
    'summary': 'This model will be use to manage Garage System.',
    'category' : 'Garage',
    'auther': 'SKYSCEND BUSINESS SOLUTIONS PVT LTD.',
    'depends':['base'],
    'data' : [
        'security/garage_security.xml',
        'security/ir.model.access.csv',
        
        'views/vehicle_view.xml',
        'views/vehicle_company_view.xml',
        'views/symptom_view.xml',
        'views/jobcard_view.xml',
        'views/customer_view.xml',
        'views/repair_view.xml',
        'views/sparepart_view.xml',
        
        
    ],
    'auto_install': False,
    'installable' : True,
    'application' : True,
    'license' : 'LGPL-3',
}