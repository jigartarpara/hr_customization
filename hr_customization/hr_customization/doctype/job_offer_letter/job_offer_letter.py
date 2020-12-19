# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
class JobOfferLetter(Document):
	def validate(self):
		if not self.skip_restriction and not self.job_application:
			frappe.throw("Job Vacancy is Mandatory")

@frappe.whitelist()
def make_employee_onboarding(source_name, target_doc=None, ignore_permissions = False):	
	doclist = get_mapped_doc("Job Offer Letter", source_name, {
			"Job Offer Letter": {
				"doctype": "Employee Onboarding Process",
				"field_map": {
					"name" : "job_offer_letter"
				}
			},
			# "Production SO Table": {
			# 	"doctype": "Paper Cup Job Order Item",
			# 	"field_map": {
			# 		"item" : "item",
			# 		"manufacture_carton": "carton",
			# 	}
			# }
		}, target_doc, ignore_permissions=ignore_permissions)
	
	return doclist
