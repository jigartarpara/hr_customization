// Copyright (c) 2020, Jigar Tarpara and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job Offer Letter', {
	refresh: function(frm) {
		// if(!cur_frm.doc.__islocal) {;
		// 	var job_vacancy = frm.add_custom_button(__('Employee Onboarding Process'), function(){
		// 		frappe.model.open_mapped_doc({
		// 			method: "hr_customization.hr_customization.doctype.job_offer_letter.job_offer_letter.make_job_offer_letter",
		// 			frm: cur_frm
		// 		})
		// 	})
		// 	job_vacancy.addClass('btn-primary')
		// }
	},
});
