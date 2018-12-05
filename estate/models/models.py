# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Estate(models.Model):
    _name = 'estate.estate'

    name = fields.Char()


class Property(models.Model):
    _name = 'estate.property'

    name = fields.Char()
    estate_id = fields.Many2one('estate.estate', ondelete='set null')

    levy_amount = fields.Float()
    partner_id = fields.Many2one('res.partner', string='Partner')
