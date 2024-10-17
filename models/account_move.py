from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    total_kg = fields.Float(string="Total Kg", compute="_compute_totals")
    total_units = fields.Float(string="Total Unidades", compute="_compute_totals")

    @api.depends("invoice_line_ids.quantity", "invoice_line_ids.product_uom_id")
    def _compute_totals(self):
        for move in self:
            total_kg = 0.0
            total_units = 0.0
            if move.invoice_line_ids:
                for line in move.invoice_line_ids:
                    if line.product_uom_id.name.lower() == "kg":
                        total_kg += line.quantity
                    elif line.product_uom_id.name.lower() == "unidad(es)":
                        total_units += line.quantity
                move.total_kg = total_kg
                move.total_units = total_units
