{
    'name': 'Garage management system',
    'summary': 'This model wil be used for Garage Management System',
    'category' : 'Garage',
    'auther': 'Gaural Makwana',
    'depends':['base','hr'],
    'data' : [
        'security/garage_security.xml',
        'security/ir.model.access.csv',
        'views/vehicle_view.xml',
        'views/customer_view.xml',
        'views/symptom_view.xml',
        'views/repair_view.xml',
        'views/jobcard_view.xml'
    ],
    'sequence': 10,
    'auto_install': False,
    'installable' : True,
    'application' : True,
    'license' : 'LGPL-3',
}