# -*- coding: utf-8 -*-

from odoo import models, fields


class StockLotNote(models.Model):
    _name = 'stock.lot.note'
    _order = 'create_date desc'

    name = fields.Text(string='Note', required=True)

    lot_id = fields.Many2one(
        comodel_name='stock.production.lot',
        string='Serial',
        required=True)
