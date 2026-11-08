from frappe import _

def get_data():
	return [
		{
			"module_name": "Accounts",
			"color": "green",
			"icon": "octicon octicon-credit-card",
			"type": "module",
			"label": _("Accounts")
		},
		{
			"module_name": "Selling",
			"color": "blue",
			"icon": "octicon octicon-briefcase",
			"type": "module",
			"label": _("Selling")
		},
		{
			"module_name": "Buying",
			"color": "orange",
			"icon": "octicon octicon-package",
			"type": "module",
			"label": _("Buying")
		},
		{
			"module_name": "Stock",
			"color": "purple",
			"icon": "octicon octicon-database",
			"type": "module",
			"label": _("Stock")
		},
		{
			"module_name": "Manufacturing",
			"color": "red",
			"icon": "octicon octicon-tools",
			"type": "module",
			"label": _("Manufacturing")
		},
		{
			"module_name": "Projects",
			"color": "yellow",
			"icon": "octicon octicon-project",
			"type": "module",
			"label": _("Projects")
		}
	]
