# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
class JobVacancy(Document):
	def validate(self):
		if not self.skip_restriction and not self.title:
			frappe.throw("Select Job Description is Mandatory")

@frappe.whitelist()
def make_job_application(source_name, target_doc=None, ignore_permissions = False):	
	doclist = get_mapped_doc("Job Vacancy", source_name, {
			"Job Vacancy": {
				"doctype": "Job Application",
				"field_map": {
					"name" : "job_vacancy"
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