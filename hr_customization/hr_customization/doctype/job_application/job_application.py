# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class JobApplication(Document):
	def validate(self):
		
		self.full_name = str(self.first_name) 
		
		if self.middle_name:
			self.full_name += " " + str(self.middle_name)
		
		if self.last_name:
			self.full_name += " " + str(self.last_name)
		
		if not self.skip_restriction and not self.job_vacancy:
			frappe.throw("Job Vacancy is Mandatory")
	
	def _family_details_template(self):
		if self.family_details_template:
			doc = frappe.get_doc("Family Details Template", self.family_details_template)
			if doc:
				return doc.family_details_parameter
	
	def _languages_known_template(self):
		if self.languages_known_template:
			doc = frappe.get_doc("Languages Known Template", self.languages_known_template)
			if doc:
				return doc.language_known_parameter
	
	def _salary_template(self):
		if self.salary_template:
			doc = frappe.get_doc("Salary Template", self.salary_template)
			if doc:
				return doc.family_details_parameter

@frappe.whitelist()
def make_job_offer_letter(source_name, target_doc=None, ignore_permissions = False):	
	doclist = get_mapped_doc("Job Application", source_name, {
			"Job Application": {
				"doctype": "Job Offer Letter",
				"field_map": {
					"name" : "job_application"
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

