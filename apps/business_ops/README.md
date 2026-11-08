# Business Operations

A small Frappe app that complements ERPNext rather than duplicating it.

- **Business Shipment** links shipping milestones to customers, suppliers, sales orders, purchase orders, and delivery notes.
- **Business Production Cycle** links light manufacturing progress to ERPNext items, BOMs, work orders, projects, and material-consumption notes.

The app is installed by `scripts/start.sh` after ERPNext. Its DocTypes are created idempotently during installation.
