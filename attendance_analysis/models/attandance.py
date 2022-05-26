from odoo import fields, models, api
from datetime import datetime, date, time


class AttendanceAnalysis(models.Model):
    _name = 'attendance.analysis'
    _description = 'Attendance Analysis Base Model'
    _rec_name = 'name_type'

    name_type = fields.Selection([
        ('by_employee', 'By Employee'),
        ('by_department', 'By Department'),
        ('by_company', 'By Company')
    ], default="by_employee")

    month = fields.Selection(
        [('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'),
         ('7', 'July'),
         ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')],
        string='Month', default="1")
    date_from = fields.Date(string="Date", default=datetime.today())
    date_to = fields.Date(string="Date", default=datetime.today())

    employee = fields.Many2many('hr.employee', string='Employee')
    year = fields.Selection([('22', '2022'), ('23', '2023'), ('24', '2024'), ('25', '2025'), ('26', '2026'),
                             ('27', '2027'),
                             ('28', '2028'), ('29', '2029'), ('30', '2030'), ('31', '2031'), ('32', '2032'),
                             ('33', '2033')], string='Year', default="22")

    # @api.depends('name_type')
    # def _compute_hide(self):
    #     # simple logic, but you can do much more here
    #     if self.name_type == 'by_employee':
    #         self.employee = True
    #     else:
    #         self.employee = False

    # def get_years(self):
    #     year_list = []
    #     for i in range(2022, 2030):
    #         year_list.append(('i', 'i'))
    #     return year_list
