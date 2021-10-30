import frappe
from frappe.utils import flt

def update_recommended_rate(self,method):
	for item in self.items:
		markup_margin_cf=frappe.db.get_value('Item', item.item_code, 'markup_margin_cf')
		if markup_margin_cf and markup_margin_cf>0:
			default_bom=frappe.db.get_value('Item', item.item_code, 'default_bom')
			
			if default_bom:
				total_cost=frappe.db.get_value('BOM', default_bom, 'total_cost')
				if total_cost and total_cost>0:
					recommend_rate_cf=flt(total_cost+((total_cost*markup_margin_cf)/100))
					if recommend_rate_cf:
						item.recommend_rate_cf=recommend_rate_cf
		