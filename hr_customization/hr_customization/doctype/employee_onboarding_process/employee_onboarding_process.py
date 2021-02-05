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
		
		if self.get('workflow_state') and self.workflow_state == "Pending For Biometric Registration"  and (not self.employee):
			frappe.throw("Couldn't Pending For Biometric Registration because employee not available")
		
		if self.get('workflow_state') and self.workflow_state == "Biometric Registration Done"  and (not self.card_number):
			frappe.throw("Couldn't Biometric Registration Done because Card Number not available")
		
		if self.get('workflow_state') and self.workflow_state == "Resources Pending"  and (not self.induction_checklist):
			frappe.throw("Couldn't Resources Pending because Resources Table not available")
		
		if self.get('workflow_state') and self.workflow_state == "Resources Provided" :
			for raw in self.induction_checklist:
				if raw.status != "Done":
					frappe.throw("Couldn't Resources Provided because Resource Status not done yet.")
