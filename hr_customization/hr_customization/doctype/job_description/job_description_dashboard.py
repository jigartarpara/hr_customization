from __future__ import unicode_literals

from frappe import _

def get_data():
    return {
        'fieldname': 'title',
        'non_standard_fieldnames': {
            'Job Vacancy': 'title',
            'Job Application': 'title',
            'Job Offer Letter': 'designation',
            'Employee Onboarding Process': 'designation',
        },
        'transactions': [
            {
                'label': _('Job Openning'),
                'items': ['Job Vacancy', 'Job Application', 'Job Offer Letter']  
            },
            {
                'label': _('Employee Onboarding'),
                'items': ['Employee Onboarding Process']
            }
            
        ]
    }