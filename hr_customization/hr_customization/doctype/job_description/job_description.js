// Copyright (c) 2020, Jigar Tarpara and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job Description', {
	refresh: function(frm) {
		if(!cur_frm.doc.__islocal) {;
			var job_vacancy = frm.add_custom_button(__('Job Vacancy'), function(){
				frappe.model.open_mapped_doc({
					method: "hr_customization.hr_customization.doctype.job_description.job_description.make_jobvacancy",
					frm: cur_frm
				})
			})
			job_vacancy.addClass('btn-primary')
		}
	}
});
