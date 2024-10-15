# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Total KG or Units",
    "summary": """
        Show total KG per order in sale order or invoices""",
    "author": "Nahe Consulting Group",
    "maintainers": ["nahe-consulting-group"],
    "website": "https://nahe.com.ar/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "15.0.2.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ["sale", "account"],
    "data": [
        "views/account_invoice_report.xml",
        "views/account_move_view.xml",
        "views/sale_order_report.xml",
        "views/sale_order_view.xml",
    ],
}
