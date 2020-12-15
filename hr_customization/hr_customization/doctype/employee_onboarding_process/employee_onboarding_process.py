# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class EmployeeOnboardingProcess(Document):
	def validate(self):
		if not self.skip_restriction and not self.job_offer_letter:
			frappe.throw("JOB Offer Letter is Mandatory")
