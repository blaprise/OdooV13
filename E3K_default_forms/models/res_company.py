# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResCompany(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'

    note_order = fields.Text(
        string="Note for Sale Order",
        translate=True,
    )

    note_quotation = fields.Text(
        string='Note for Quotation',
        translate=True,
    )

    note_invoice = fields.Text(
        string='Note for Invoice',
        translate=True,
    )

    bank_note = fields.Html(
        string='Note for Bank Account',
        translate=True,
    )
