# Docker Setup

This project follows Frappe's recommended Docker approach. Use [frappe_docker](https://github.com/frappe/frappe_docker) for production/dev.

## Quick References
- Devcontainer: https://github.com/frappe/frappe_docker/blob/main/docs/05-development/01-development.md
- Build custom image: https://frappe.github.io/frappe_docker/02-setup/02-build-setup.html
- Environment variables: https://frappe.github.io/frappe_docker/02-setup/04-env-variables.html

## Example apps.json entry
```json
[
  {"url": "https://github.com/frappe/frappe", "branch": "version-15"},
  {"url": "https://github.com/frappe/erpnext", "branch": "version-15"},
  {"url": "/path/to/erp_core", "branch": "main"}
]
```
(Or use git URL for your repo)

## Local dev compose (template)
Copy from frappe_docker and mount this app into bench apps directory.
