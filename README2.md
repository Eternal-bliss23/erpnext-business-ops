# Business ERP

This project is a Dockerized, open-source ERP deployment based on **Frappe Framework and ERPNext**. ERPNext already provides the core modules requested:

| Business need | ERPNext workflow |
| --- | --- |
| Accounting and cash flow | Chart of Accounts, Journal Entry, Payment Entry, bank reconciliation, General Ledger, Balance Sheet, Profit and Loss, Cash Flow |
| Customers, sales, inventory | Customer, Quotation, Sales Order, Delivery Note, Sales Invoice, warehouses, stock reports |
| Suppliers and incoming goods | Supplier, Purchase Order, Purchase Receipt, Purchase Invoice, Payment Entry |
| Shipments | Delivery Note plus the included **Business Shipment** tracker |
| Light manufacturing | BOM, Work Order, Job Card, Stock Entry, material consumption plus **Business Production Cycle** notes |
| Projects and time | Project, Task, Timesheet, expenses, billing, profitability |

## Deployment

1. Install Docker Engine with Docker Compose v2. The scripts perform a preflight check and stop with a clear message when it is unavailable. This machine did not have Docker available when this workspace was created.
2. Copy and edit the environment file:

   ```bash
   cd /home/daniel-park/Downloads/test1
   cp .env.business.example .env.business
   # Set DB_PASSWORD and ADMIN_PASSWORD to unique, long values.
   ```

3. Start the complete stack and create the site:

   ```bash
   ./scripts/start.sh
   ```

4. Open `http://localhost:8080` and sign in as `Administrator` with `ADMIN_PASSWORD` from `.env.business`.

The startup script builds a local image containing `business_ops`, uses the official Frappe Docker production base Compose file plus MariaDB, Redis, and no-proxy overrides, then installs both ERPNext and the custom app.

## First-day configuration

1. In the Setup Wizard, create the company, currency, fiscal year, and default accounts.
2. Create users and grant least-privilege roles such as Accounts User, Sales User, Purchase User, Stock User, Manufacturing User, and Projects User.
3. Add warehouses, items, customers, suppliers, price lists, taxes, payment terms, and approval rules.
4. Test a complete sale: Sales Order -> Delivery Note -> Sales Invoice -> Payment Entry. Verify the General Ledger and stock balance.
5. Test a production cycle: BOM -> Work Order -> Stock Entry / Job Card. Use Business Production Cycle for operational status notes.
6. Set backup, update, and access-control procedures before entering live financial data.

## Operations

Render the resolved Compose file without starting containers:

```bash
./scripts/render-compose.sh
```

Stop the stack while retaining the named data volumes:

```bash
docker compose --env-file .env.business -f compose.generated.yaml -p business-erp down
```

Do not run `down --volumes` unless you explicitly intend to delete ERP data.

## Sources

- ERPNext's README describes the included Accounting, Order Management, Manufacturing, and Projects capabilities.
- Frappe Docker is the official Docker deployment repository. This project follows its documented production composition model rather than the disposable `pwd.yml` demo.
