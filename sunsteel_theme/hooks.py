# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sunsteel_theme"
app_title = "Sunsteel Theme"
app_publisher = "GreyCube Technologies"
app_description = "Customization of theme for sunsteel"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sunsteel_theme/css/sunsteel_theme.css"
# app_include_js = "/assets/sunsteel_theme/js/sunsteel_theme.js"

# include js, css files in header of web template
# web_include_css = "/assets/sunsteel_theme/css/sunsteel_theme.css"
web_include_js = "/assets/sunsteel_theme/js/core.min.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sunsteel_theme.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sunsteel_theme.install.before_install"
# after_install = "sunsteel_theme.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sunsteel_theme.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Quotation": {
		"validate": "sunsteel_theme.quotation_controller.update_recommended_rate",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sunsteel_theme.tasks.all"
# 	],
# 	"daily": [
# 		"sunsteel_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"sunsteel_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sunsteel_theme.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sunsteel_theme.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sunsteel_theme.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sunsteel_theme.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sunsteel_theme.task.get_dashboard_data"
# }

