app_name = "pushtisanskar_website"
app_title = "Pushtisanskar Website"
app_publisher = "Sanskar Technolab"
app_description = "Pushtisanskar website"
app_email = "darshit@sanskartechnolab.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "pushtisanskar_website",
# 		"logo": "/assets/pushtisanskar_website/logo.png",
# 		"title": "Pushtisanskar Website",
# 		"route": "/pushtisanskar_website",
# 		"has_permission": "pushtisanskar_website.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pushtisanskar_website/css/pushtisanskar_website.css"
# app_include_js = "/assets/pushtisanskar_website/js/pushtisanskar_website.js"

# include js, css files in header of web template
# web_include_css = "/assets/pushtisanskar_website/css/pushtisanskar_website.css"
# web_include_js = "/assets/pushtisanskar_website/js/pushtisanskar_website.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "pushtisanskar_website/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "pushtisanskar_website/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "pushtisanskar_website.utils.jinja_methods",
# 	"filters": "pushtisanskar_website.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "pushtisanskar_website.install.before_install"
# after_install = "pushtisanskar_website.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "pushtisanskar_website.uninstall.before_uninstall"
# after_uninstall = "pushtisanskar_website.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "pushtisanskar_website.utils.before_app_install"
# after_app_install = "pushtisanskar_website.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "pushtisanskar_website.utils.before_app_uninstall"
# after_app_uninstall = "pushtisanskar_website.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pushtisanskar_website.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pushtisanskar_website.tasks.all"
# 	],
# 	"daily": [
# 		"pushtisanskar_website.tasks.daily"
# 	],
# 	"hourly": [
# 		"pushtisanskar_website.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pushtisanskar_website.tasks.weekly"
# 	],
# 	"monthly": [
# 		"pushtisanskar_website.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "pushtisanskar_website.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pushtisanskar_website.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "pushtisanskar_website.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["pushtisanskar_website.utils.before_request"]
# after_request = ["pushtisanskar_website.utils.after_request"]

# Job Events
# ----------
# before_job = ["pushtisanskar_website.utils.before_job"]
# after_job = ["pushtisanskar_website.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"pushtisanskar_website.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    {
        "dt": "Builder Settings",
    },
    #  {
    #     "dt": "Block Template",
    # },
    # {
    #     "dt": "Builder Component",
    # },
    # {
    #     "dt": "Builder Page",
    # },    
    # {
    #     "dt": "Builder Client Script",
    # },
]