"""Install custom, operational DocTypes without replacing ERPNext workflows.

ERPNext remains the system of record for finance, inventory, sales, purchasing,
manufacturing, projects, and timesheets. These two DocTypes add a light
operations layer for shipment milestones and production-cycle notes.
"""

from __future__ import annotations

import frappe


def _field(fieldname, label, fieldtype, **kwargs):
    return {"fieldname": fieldname, "label": label, "fieldtype": fieldtype, **kwargs}


def _create_doctype(name, fields, title_field, description):
    if frappe.db.exists("DocType", name):
        return
    frappe.get_doc(
        {
            "doctype": "DocType",
            "name": name,
            "module": "Business Operations",
            "custom": 0,
            "istable": 0,
            "editable_grid": 1,
            "track_changes": 1,
            "autoname": "format:{####}",
            "title_field": title_field,
            "description": description,
            "fields": fields,
            "permissions": [
                {"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1, "report": 1, "export": 1},
                {"role": "Stock User", "read": 1, "write": 1, "create": 1, "report": 1},
                {"role": "Manufacturing User", "read": 1, "write": 1, "create": 1, "report": 1},
            ],
        }
    ).insert(ignore_permissions=True)


def after_install():
    if not frappe.db.exists("Module Def", "Business Operations"):
        frappe.get_doc({"doctype": "Module Def", "module_name": "Business Operations", "app_name": "business_ops"}).insert(ignore_permissions=True)

    _create_doctype(
        "Business Shipment",
        [
            _field("shipment_reference", "Shipment Reference", "Data", reqd=1, in_list_view=1),
            _field("status", "Status", "Select", options="Planned\nReady to Ship\nIn Transit\nDelivered\nDelayed\nCancelled", default="Planned", in_list_view=1),
            _field("customer", "Customer", "Link", options="Customer", in_list_view=1),
            _field("supplier", "Supplier", "Link", options="Supplier"),
            _field("sales_order", "Sales Order", "Link", options="Sales Order"),
            _field("purchase_order", "Purchase Order", "Link", options="Purchase Order"),
            _field("delivery_note", "Delivery Note", "Link", options="Delivery Note"),
            _field("carrier", "Carrier", "Data"),
            _field("tracking_number", "Tracking Number", "Data"),
            _field("expected_date", "Expected Delivery", "Date"),
            _field("actual_delivery_date", "Actual Delivery", "Date"),
            _field("notes", "Operational Notes", "Text Editor"),
        ],
        "shipment_reference",
        "Track customer and supplier shipment milestones alongside standard ERPNext orders and delivery documents.",
    )

    _create_doctype(
        "Business Production Cycle",
        [
            _field("cycle_reference", "Cycle Reference", "Data", reqd=1, in_list_view=1),
            _field("status", "Status", "Select", options="Planned\nIn Progress\nQuality Check\nCompleted\nOn Hold\nCancelled", default="Planned", in_list_view=1),
            _field("item", "Finished Item", "Link", options="Item", in_list_view=1),
            _field("work_order", "Work Order", "Link", options="Work Order"),
            _field("bom_no", "Bill of Materials", "Link", options="BOM"),
            _field("project", "Project", "Link", options="Project"),
            _field("planned_start_date", "Planned Start", "Date"),
            _field("planned_end_date", "Planned End", "Date"),
            _field("actual_start_date", "Actual Start", "Date"),
            _field("actual_end_date", "Actual End", "Date"),
            _field("material_consumption_notes", "Material Consumption Notes", "Text Editor"),
            _field("quality_notes", "Quality Notes", "Text Editor"),
        ],
        "cycle_reference",
        "Provide a concise operational view of light-manufacturing cycles while ERPNext Work Orders and Stock Entries remain authoritative.",
    )
    frappe.db.commit()
