# Copyright (c) 2013, GreyCube Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data = get_data(filters)	

	return columns, data
def get_columns():
	return [
 {
   "fieldname": "item_code",
   "fieldtype": "Link",
   "label": "Item",
   "options": "Item",
   "width": 250
  },
  {
   "fieldname": "item_name",
   "fieldtype": "Data",
   "label": "Name",
   "width": 200
  },	
  {
   "fieldname": "item_group",
   "fieldtype": "Link",
   "label": "Group",
   "options": "Item Group",
   "width": 130
  },
  {
   "fieldname": "default_bom",
   "fieldtype": "LInk",
   "label": "Default BOM",
   "options": "BOM",   
   "width": 150
  },			
  {
   "fieldname": "total_cost",
   "fieldtype": "float",
   "label": "Total Cost",
   "width": 120
  },
  {
   "fieldname": "markup_margin_cf",
   "fieldtype": "Percentage",
   "label": "Margin%",
   "width": 100
  },
  {
   "fieldname": "recommend_rate_cf",
   "fieldtype": "Float",
   "label": "Recommended Rate",
   "width": 140
  }
		]

def get_data(filters):
	data = []
	data = frappe.db.sql("""SELECT 
	item.item_code,
	item.item_name,
	item.item_group,
	item.default_bom,
	bom.total_cost,
	item.markup_margin_cf,
	(bom.total_cost + (bom.total_cost * item.markup_margin_cf ) * 100 ) as recommend_rate_cf 
	from `tabItem` as item 
	inner join `tabBOM` as bom 
	on item.default_bom =bom.name""",as_dict=True)		
	return data			