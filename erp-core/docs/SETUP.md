# Setup Guide - BizERP (erp_core)

This project is designed to be installed as a Frappe app. The recommended approach follows official Frappe/ERPNext documentation.

## Prerequisites
- Linux/macOS (or WSL2 on Windows)
- Python 3.10+ (matches Frappe v14/v15), Node.js 18+, Yarn
- MariaDB/Postgres, Redis
- Git
- Docker (optional, recommended for containerized dev)

## Option 1: Using frappe_docker (Recommended for Docker/Devcontainers)

1. Clone frappe_docker:
```bash
git clone https://github.com/frappe/frappe_docker.git
cd frappe_docker
```

2. For development, use devcontainer workflow as per [Frappe Docker docs](https://github.com/frappe/frappe_docker/blob/main/docs/05-development/01-development.md). Copy `devcontainer-example` to `.devcontainer/` and open in VS Code with Remote Containers.

3. Inside the dev container (or bench environment), get and install this app:
```bash
# From bench directory (e.g., /workspace/development/frappe-bench)
bench get-app /path/to/erp_core  # or git URL
bench --site development.localhost install-app erp_core
bench start
```

Or build custom image with `apps.json` including this repo (see Build Setup docs).

## Option 2: Manual Bench Installation (Non-Docker)

Follow [Frappe Framework Installation](https://docs.frappe.io/framework/user/en/installation):
```bash
pipx install frappe-bench  # or venv
bench init frappe-bench --frappe-branch version-15
cd frappe-bench
bench new-site mysite.localhost
bench get-app https://github.com/frappe/erpnext  # optional, for full parity
# Add our app
bench get-app file:///home/daniel-park/Downloads/test1  # or copy to apps/
bench --site mysite.localhost install-app erp_core
bench start
```

## Docker Compose (Quick Reference)
See `docker/` directory for example compose files. For full setup, prefer `frappe_docker`.

## First Run
1. Open site (e.g., http://mysite.localhost:8000)
2. Login as Administrator
3. Configure Company, Chart of Accounts, Warehouses, etc.
4. Start using modules: Accounts, Selling, Buying, Stock, Manufacturing, Projects
