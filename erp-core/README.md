# BizERP - Comprehensive Open Source ERP System

A Python-based, Frappe/ERPNext-inspired comprehensive ERP system built to run an all-in-one business. Covers accounting, order management/inventory, suppliers/shipments, light manufacturing, and project management with timesheets.

## Core Modules

- **Accounting**: Chart of Accounts, Journal Entries, Sales/Purchase Invoices, Payments, Taxes, Cash Flow, Financial Reports (Balance Sheet, P&L, Trial Balance, General Ledger)
- **Order Management**: Customers, Sales Orders, Quotations, Delivery Notes, Inventory Tracking (Warehouses, Items, Stock Ledger, Bins)
- **Purchasing & Suppliers**: Purchase Orders, Purchase Invoices, Supplier Master, Shipments/Delivery Tracking
- **Manufacturing**: BOMs, Work Orders, Material Consumption, Production Cycles/Job Cards, Stock Transfers for WIP/FG
- **Project Management**: Projects, Tasks, Timesheets, Milestones, Dependencies, Time Billing
- **CRM/Contacts, HR-lite, Assets** (extensible)

## Tech Stack

- **Framework**: [Frappe Framework](https://frappeframework.com/) (Python) - recommended per Frappe docs
- **App Name**: `erp_core` (installable Frappe app)
- **Database**: MariaDB/Postgres (via Frappe)
- **Cache/Queue**: Redis
- **Containerization**: Docker (see `docker/` and recommended `frappe_docker` workflow)

## Quick Start (Recommended: Use frappe_docker)

Following Frappe's recommended approach:

1. Clone [frappe_docker](https://github.com/frappe/frappe_docker) alongside or use it as dev environment
2. Copy this app into your bench's `apps/` or build a custom image with `apps.json` including this repo
3. Create site and install app: `bench new-site yoursite.localhost && bench --site yoursite.localhost install-app erp_core`
4. Start: `bench start`

See `docs/SETUP.md` for detailed instructions.

## Local Development with Docker (Devcontainer)

Use frappe_docker's devcontainer workflow (see Frappe Docker docs). Mount this repo into bench apps.

## Dockerized ERPNext Deployment

This repository also contains a self-hosted ERPNext deployment with the
`business_ops` Frappe app. It uses the official Frappe Docker production
Compose base with MariaDB, Redis, and a locally built custom image.

### Prerequisites

- Docker Engine and Docker Compose v2

### Start the ERP

```bash
cp .env.business.example .env.business
# Edit .env.business and replace DB_PASSWORD and ADMIN_PASSWORD.
./scripts/start.sh
```

Open `http://localhost:8080` and sign in as `Administrator` with the password
set in `ADMIN_PASSWORD`.

The first startup builds the local image, starts the Frappe services, creates
the configured site, and installs both `erpnext` and `business_ops`.

### Included Operations Add-On

`business_ops` adds two operational DocTypes without replacing ERPNext's core
financial and inventory records:

- **Business Shipment**: shipment status, carrier, tracking number, expected
  delivery, and links to customer/supplier orders and delivery notes.
- **Business Production Cycle**: production status, item, BOM, work order,
  project, dates, and material-consumption or quality notes.

Use ERPNext's native modules as the system of record for accounting, sales,
purchasing, inventory, manufacturing, projects, and timesheets. For first-day
configuration and operational commands, see `README.business.md`.

## License

MIT
