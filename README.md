# ERP Project Collection

This folder contains two separate Frappe-based ERP implementations:

- [`erpnext-business-ops/`](erpnext-business-ops/): the recommended Dockerized
  ERPNext deployment. ERPNext supplies the mature core ERP modules, and the
  included `business_ops` app adds shipment and production-cycle tracking.
- [`erp-core/`](erp-core/): a standalone custom Frappe app that implements its
  own ERP DocTypes for accounting, orders, stock, manufacturing, projects, and
  timesheets.

The projects have intentionally been kept separate because their functional
scope overlaps. See each project's README before choosing one to deploy.
