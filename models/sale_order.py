from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_kg = fields.Float(string="Total Kg", compute="_compute_totals")
    total_units = fields.Float(string="Total Unidades", compute="_compute_totals")

    @api.depends("order_line.product_uom_qty", "order_line.product_uom")
    def _compute_totals(self):
        for order in self:
            total_kg = 0.0
            total_units = 0.0
            for line in order.order_line:
                if line.product_uom.name.lower() == "kg":
                    total_kg += line.product_uom_qty
                elif line.product_uom.name.lower() == "unidad(es)":
                    total_units += line.product_uom_qty
            order.total_kg = total_kg
            order.total_units = total_units
