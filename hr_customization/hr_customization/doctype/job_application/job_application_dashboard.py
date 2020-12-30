from __future__ import unicode_literals

from frappe import _

def get_data():
    return {
        'fieldname': 'name',
        'non_standard_fieldnames': {
            'Job Offer Letter': 'job_application',
            'Employee Onboarding Process': 'job_application'
        },
        'transactions': [
            {
                'items': ['Job Offer Letter', 'Employee Onboarding Process']  
            }
            
        ]
    }