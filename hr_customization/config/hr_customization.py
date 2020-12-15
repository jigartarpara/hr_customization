from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Recruitment"),
			"items": [
				{
					"type": "doctype",
					"name": "Job Description",
					"description": _("Job Description")
				},
				{
					"type": "doctype",
					"name": "Job Vacancy",
					"description": _("Job Vacancy")
				},
				{
					"type": "doctype",
					"name": "Job Application",
					"description": _("Job Application"),
				},
				{
					"type": "doctype",
					"name": "Job Offer Letter",
					"description": _("Job Offer Letter"),
				},
				{
					"type": "doctype",
					"name": "Employee Onboarding Process",
					"description": _("Employee Onboarding Process"),
				}
			]
		},
	]
