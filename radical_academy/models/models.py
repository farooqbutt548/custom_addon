# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RadicalAcademy(models.Model):
    _name = 'radical.academy'
    _description = 'this will provide info about academy'

    name = fields.Char(string='Name', help="Student Name")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),

    ])
    age = fields.Integer(string="Age")
    experience = fields.Integer(string="Year's of Experience")
    lectures = fields.Integer(string="Lectures")
    is_virtual_school = fields.Boolean(string="Virtual school ??")
    subject = fields.Char(string="Subject")
    school_id = fields.Many2one("radical.student", string="School ID")
    # is_virtual = fields.Boolean()

    school_list = fields.One2many('radical.student', 'ahmed_id', string='School List')
    student_list = fields.Many2many("radical.student", string="Student")


class RadicalStudent(models.Model):
    _name = 'radical.student'

    ustad = fields.Char(string='Waqas')
    thatha = fields.Char(string='thatha')
    gonga = fields.Char(string='gonga')
    ahmed_id = fields.Many2one('radical.academy', string='ahmed')


    # class PatientProfiles(models.Model):
    #     _inherit = "hospital.patient"














# value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
