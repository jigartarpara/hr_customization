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
        {
            "label": _("Employee"),
            "items": [
                {
                    "type": "doctype",
                            "name": "Employee",
                                    "description": _("Employee")
                },
            ]
        },
        {
            "label": _("Employee Life Cycle"),
            "items": [
                {
                    "type": "doctype",
                            "name": "Employee",
                                    "description": _("Employee Details")
                },
                {
                    "type": "doctype",
                            "name": "Employee Onboarding Process",
                                    "description": _("Employee Onboarding Process")
                },
                {
                    "type": "doctype",
                            "name": "Employee Skill Map",
                                    "description": _("Employee Skill Map")
                },
                {
                    "type": "doctype",
                            "name": "Employee Promotion",
                                    "description": _("Employee Promotions")
                },
                {
                    "type": "doctype",
                            "name": "Employee Transfer",
                                    "description": _("Employee Transfer Details")
                },
                {
                    "type": "doctype",
                            "name": "Employee Separation",
                                    "description": _("Employee Separation Details")
                },
            ]
        },
        {
            "label": _("Leaves"),
            "items": [
                {
                    "type": "doctype",
                            "name": "Leave Application",
                                    "description": _("Leave Application")
                },
                {
                    "type": "doctype",
                            "name": "Leave Allocation",
                                    "description": _("Leave Allocation")
                }
            ]
        },
        {
            "label": _("Performance"),
            "items": [
                {
                    "type": "doctype",
                            "name": "Appraisal",
                                    "description": _("Appraisal")
                },
            ]
        },
        {
            "label": _("Shift Management"),
            "items": [
                {
                    "type": "doctype",
                            "name": "Shift Request",
                                    "description": _("Shift Request")
                },
                {
                    "type": "doctype",
                            "name": "Shift Assignment",
                                    "description": _("Shift Assignment")
                },
                {
                    "type": "doctype",
                            "name": "Update Shift Request",
                                    "description": _("Update Shift Request")
                }
            ]
        },
        # {
        # 	"label": _("Approval"),
        # 	"items": [
        # 		{
        # 			"type": "doctype",
        # 			"name": "Gate Pass",
        # 			"description": _("Gate Pass")
        # 		},
        # 	]
        # },
        {
            "label": _("Reports"),
            "items": [
                {
                    "type": "report",
                    "name": "Employee Birthday",
                    "description": _("Employee Birthday"),
                    "is_query_report": True,
                    "reference_doctype": "Employee",
                },
                {
                    "type": "report",
                    "name": "Attendance Tracker",
                    "description": _("Attendance Tracker"),
                    "is_query_report": True,
                    "reference_doctype": "Attendance",
                },
                # {
                #     "type": "doctype",
                #     "name": "Holiday List",
                #     "description": _("Holiday List")
                # },
                {
                    "type": "report",
                    "name": "Monthly Attendance Sheet",
                    "description": _("Monthly Attendance Sheet"),
                    "is_query_report": True,
                    "reference_doctype": "Attendance",
                },
                # {
                #     "type": "report",
                #     "name": "Attendance Log Report",
                #     "description": _("Attendance Log Report"),
                #     "is_query_report": True,
                #     "reference_doctype": "Attendance Log",
                # },
            ]
        }
    ]
