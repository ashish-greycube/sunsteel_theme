from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
	config = [
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"name": "Recommended Selling Price",
					"is_query_report": True,
					"doctype": "Item"
				}
			]
		}
		]
	return config
	