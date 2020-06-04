# -*- coding: utf-8 -*-

from odoo import fields, models, api


class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = 'account.move'

    note_inv = fields.Text(
        related='company_id.note_invoice',
        string="Note for Invoice",
    )
