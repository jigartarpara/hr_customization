// Copyright (c) 2020, Jigar Tarpara and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job Vacancy', {
	refresh: function(frm) {
		if(!cur_frm.doc.__islocal) {;
			var job_vacancy = frm.add_custom_button(__('Job Application'), function(){
				frappe.model.open_mapped_doc({
					method: "hr_customization.hr_customization.doctype.job_vacancy.job_vacancy.make_job_application",
					frm: cur_frm
				})
			})
			job_vacancy.addClass('btn-primary')
		}
	}
});
