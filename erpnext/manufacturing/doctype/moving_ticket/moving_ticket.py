# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MovingTicket(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		colour_code: DF.Link | None
		colour_name: DF.Data | None
		customer_code: DF.Link | None
		customer_name: DF.Data | None
		date: DF.Date | None
		gramasi_kain_body: DF.Data | None
		gramasi_kain_rib: DF.Data | None
		jenis_kain: DF.Data | None
		moving_ticket_no: DF.ReadOnly | None
		po_no_customer: DF.Data | None
		production_order: DF.Link | None
		size_benang: DF.Data | None
	# end: auto-generated types
	pass
