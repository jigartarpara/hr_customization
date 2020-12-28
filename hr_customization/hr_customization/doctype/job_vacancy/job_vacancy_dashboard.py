from __future__ import unicode_literals

from frappe import _

def get_data():
    return {
        'fieldname': 'name',
        'non_standard_fieldnames': {
            'Job Application': 'job_vacancy',
            'Job Offer Letter': 'name',
            'Employee Onboarding Process': 'designation'
        },
        'dynamic_links': {
            'name': ['Job Vacancy', 'job_offer_letter']
        },
        'transactions': [
            {
                'label': _('Job Openning'),
                'items': ['Job Application', 'Job Offer Letter']  
            },
            {
                'label': _('Employee Onboarding'),
                'items': ['Employee Onboarding Process']
            }
            
        ]
    }