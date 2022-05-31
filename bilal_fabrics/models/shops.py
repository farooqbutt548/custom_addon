from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError, UserError


class Bilalfabrics(models.Model):
    _name = "bilal.fabrics"

    # _inherits = {'bilal.bill': 'Many2one field of this model'}
    # _inherit = ['mail.thread', 'mail.activity.mixin']             # used for Chatter box(keep Track)

    def delete_one2many(self):
        for record in self:
            if record.bill_detail:
                record.bill_detail = [(5, 0, 0)]
                return {
                    'effect': {
                        'fadeout': 'fast',
                        'type': 'rainbow_man',
                        'message': 'Bill data has been deleted successfully '
                    }
                }


    def do_unpaid(self):
        for rec in self:
            rec.status = 'unpaid'

    def do_paid(self):
        for rec in self:
            rec.status = 'paid'

    # def compute_bill_count(self):  # Computed field for Bill Count
    #     bill_count = self.env['bilal.fabrics'].search_count([])
    #     self.bill_count = bill_count

    # For Report Print
    def report_print_button(self):
        return self.env.ref('bilal_fabrics.bilal_bill_qweb_report').report_action(self)

    # Constraints of name to write 'Luqman'
    @api.constrains('name')
    def name_constraint(self):
        for record in self:
            if record.name == "Luqman":
                raise ValidationError(_("The Luqman is Bilals's brother not a Customer"))

                # Left amount after Paid amount

    @api.depends('total_amount', 'paid_amount')
    def left_amount_func(self):
        for record in self:
            record.left_amount = (record.total_amount) - (record.paid_amount)

    @api.model
    def create(self, vals):
        if vals.get("seq_num", _('New')) == ('New'):
            vals['seq_num'] = self.env['ir.sequence'].next_by_code('bill.seq.no') or _('New')
        num = super(Bilalfabrics, self).create(vals)
        return num

    def unlink(self):  # Record deleting Condition
        for rec in self:
            if rec.bill_type == 'credit':
                raise UserError(_("Record can't be deleted until 'Credit' type."))
        return super(Bilalfabrics, self).unlink()

    name = fields.Char(string="Name", track_visibility='always')
    empty = fields.Char(string=".", readonly='1')
    phone = fields.Char(string="Phone No")
    address = fields.Char(string="Address", default="Jhang")
    date = fields.Date(string="Date", default=datetime.today())
    bill_type = fields.Selection([
        ('debit', 'Debit'),
        ('credit', 'Credit'),
    ], default="debit", track_visibility='always')

    seller = fields.Selection([
        ('bilal', 'Bilal Sardar'),
        ('hamza', 'Hamza'),
        ('putin', 'Vladimir Putin'),
    ], default="bilal", track_visibility='always')
    status = fields.Selection([('paid', 'Paid'), ('unpaid', 'Unpaid')], string="Status", default="paid")
    # bill_count = fields.Char(string="Bill # ", compute='compute_bill_count')  # computed fields
    user_company = fields.Many2one('res.company', string='company', default=lambda self: self.env.user.company_id.id)

    total_amount = fields.Integer()
    paid_amount = fields.Integer()
    left_amount = fields.Integer(compute='left_amount_func')

    seq_num = fields.Char(string="Seq No.", readonly=True, copy=False, index=True, default=lambda self: _('New'))

    bill_detail = fields.One2many('bilal.bill', 'connecting_field', string="Bill-Detail")  # one2many


class BillDetail(models.Model):
    _name = 'bilal.bill'

    # _rec_name = 'product'

    connecting_field = fields.Many2one('bilal.fabrics', string="Bill-ID")
    product = fields.Many2one('bilal.products', string="Items")  # many2one
    description = fields.Char(string="Detail", related="product.product_description")
    product_qty = fields.Float(string="Qty")
    unit_price = fields.Integer(string="Unit-Price", related="product.product_price")
    discount = fields.Integer(string="Discount")
    sequence = fields.Integer(string="Seq.")  # for drag and drop the records
    sub_total = fields.Integer(string="Sub-Total", compute='oncompute_price')

    # Api depend
    @api.depends('product_qty', 'unit_price', 'discount')
    def oncompute_price(self):
        for record in self:
            record.sub_total = (record.product_qty * (record.unit_price - record.discount))

            # Api Onchange
    # sub_total = fields.Integer(string="Sub-Total")
    # @api.onchange('product_qty', 'unit_price', 'discount')
    # def _onchange_price(self):
    #     self.sub_total = (self.product_qty * (self.unit_price - self.discount))

    # def total_bill (self, *args):
    #     total_amount = 0
    #     for i in args:
    #         total_amount += i
    #     return total_amount
    # grands_total = total_bill(sub_total)
