# -*- coding: utf-8 -*-

from odoo import fields, models, api


class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    note_ord = fields.Text(
        related='company_id.note_order',
        string="Note for Sale Order",
    )

    note_qou = fields.Text(
        related='company_id.note_quotation',
        string="Note for Quotation",
    )
