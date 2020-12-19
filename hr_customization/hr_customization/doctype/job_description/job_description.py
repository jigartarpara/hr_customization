# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
class JobDescription(Document):
	pass

@frappe.whitelist()
def make_jobvacancy(source_name, target_doc=None, ignore_permissions = False):	
	doclist = get_mapped_doc("Job Description", source_name, {
			"Job Description": {
				"doctype": "Job Vacancy",
				"field_map": {
					"name" : "title"
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