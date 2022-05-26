# -*- coding: utf-8 -*-

from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    #
    name = fields.Char(string='Name', required=True, help="Patient Name")
    age = fields.Integer(string='Age', required=True)
    phone_number = fields.Char(string='Phone', required=True)
    address = fields.Char(string='Address', required=True)
    is_virtual_checkup = fields.Boolean(string="Virtual Checkup ??",
                                        help="This is boolean setup to" " check either you want" "'Virtual Check-up' or 'not'",
                                        default="true")
    establish_date = fields.Date(string="Establish Date",
                                required="True")
    open_date = fields.Datetime(string="Open Date",
                                default=fields.Datetime.now())
    documents = fields.Binary(string="Document")
    documents_name = fields.Char(string="File Name")
    patient_image = fields.Image(string="Patient Image", max_width=100,
                                 max_height=100,)
    patient_description = fields.Html(string="Description")
    # note = fields.Text(string='Discrpition')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='Male')

    note = fields.Text(string='Description')
    #     help="The 'Internal Type' is used for features available on " \
    #          "different types of accounts: liquidity type is for cash or bank accounts" \
    #          ", payable/receivable is for vendor/customer accounts.")
    # internal_group = fields.Selection([
    #     ('equity', 'Equity'),
    #     ('asset', 'Asset'),
    #     ('liability', 'Liability'),
    #     ('income', 'Income'),
    #     ('expense', 'Expense'),
    #     ('off_balance', 'Off Balance'),
    # ], string="Internal Group",
    #     required=True,
    #     help="The 'Internal Group' is used to filter accounts based on the internal group set on the account type.")
    # note = fields.Text(string='Description')

    # name = fields.Char(string='Name', required=true, )
    # value = fields.Integer(string='age', required=true)
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    #     ('other', 'Other'),
    # ], required=True, default='male',
    # #     help="The 'Internal Type' is used for features available on " \
    #          "different types of accounts: liquidity type is for cash or bank accounts" \
    #          ", payable/receivable is for vendor/customer accounts.")
    # internal_group = fields.Selection([
    #     ('equity', 'Equity'),
    #     ('asset', 'Asset'),
    #     ('liability', 'Liability'),
    #     ('income', 'Income'),
    #     ('expense', 'Expense'),
    #     ('off_balance', 'Off Balance'),
    # ], string="Internal Group",
    #     required=True,
    #     help="The 'Internal Group' is used to filter accounts based on the internal group set on the account type.")

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
