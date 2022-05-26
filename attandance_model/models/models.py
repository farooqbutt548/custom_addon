# -*- coding: utf-8 -*-

from odoo import models, fields, api


class attandance_model(models.Model):
    _name = 'attandance.model'
    _description = 'Attendance Model'

    employee = fields.Char(string="Employee")
    checkin = fields.Char(string="Check-In")
    checkout = fields.Char(string="Check-Out")
    workinghours = fields.Char(string="Working hours")
    # check = fields.Boolean()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
