# Copyright (c) 2013, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"fieldname": "employee",
			"label": "Employee",
			"fieldtype": "Link",
			"options": "Employee"
		},
		{
			"fieldname": "attendance",
			"label": "Attendance",
			"fieldtype": "Link",
			"options": "Attendance"
		},
		{
			"fieldname": "gatepass",
			"label": "Gate Pass",
			"fieldtype": "Link",
			"options": "Gate Pass"
		},
		{
			"fieldname": "overtime_application",
			"label": "Overtime Application",
			"fieldtype": "Link",
			"options": "Overtime Application"
		}
	]

def get_data(filters):
	condition = ""
	condition2 = ""
	
	if filters.get("employee"):
		condition2 += " and attendance.employee = '{0}' ".format(filters.get("employee")) 
	
	if filters.from_date:
		condition2 += " and attendance.attendance_date >= '{0}' ".format(filters.from_date)
		condition2 += " and gate_pass.date >= '{0}' ".format(filters.from_date)
		condition += " and overtime.request_date >= '{0}' ".format(filters.from_date)

	if filters.to_date:
		condition2 += " and attendance.attendance_date <='{0}' ".format(filters.to_date)
		condition2 += " and gate_pass.date <='{0}' ".format(filters.to_date)
		condition += " and overtime.request_date <='{0}' ".format(filters.to_date)
	
	data = frappe.db.sql("""
		select 
			attendance.employee, 
			attendance.attendance, 
			attendance.gate_pass, 
			overtime.name
		from
			(
				select
					attendance.employee, attendance.name as attendance, gate_pass.name as gate_pass
				from
					`tabAttendance` as attendance
				left join
					`tabGate Pass` as gate_pass
				on
					attendance.employee = gate_pass.employee
				where 
					1 = 1 {1}
			) as attendance
		left join 
			`tabOvertime Application` as overtime
		on
			attendance.employee = overtime.employee
		where
			1=1 {0}
	""".format(condition,condition2))
	return data
