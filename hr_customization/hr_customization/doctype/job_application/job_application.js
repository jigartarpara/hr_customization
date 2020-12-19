// Copyright (c) 2020, Jigar Tarpara and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job Application', {
	family_details_template: function(frm) {
		frappe.call({
			"method": "_family_details_template",
			doc: cur_frm.doc,
			callback: function (r) {
				if(r.message){

					r.message.forEach(function(element) {
						var c = frm.add_child("family_details");
						c.name1 = element.name1;
					});
					refresh_field("family_details");
				}	
			}
		})
	},
	languages_known_template: function(frm) {
		frappe.call({
			"method": "_languages_known_template",
			doc: cur_frm.doc,
			callback: function (r) {
				if(r.message){

					r.message.forEach(function(element) {
						var c = frm.add_child("languages_known");
						c.language = element.parameter;
					});
					refresh_field("languages_known");
				}	
			}
		})
	},
	salary_template: function(frm) {
		frappe.call({
			"method": "_salary_template",
			doc: cur_frm.doc,
			callback: function (r) {
				if(r.message){

					r.message.forEach(function(element) {
						var c = frm.add_child("salary_structure_table");
						c.parameter = element.parameter;
					});
					refresh_field("salary_structure_table");
				}	
			}
		})
	},
});
