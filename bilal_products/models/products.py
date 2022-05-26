from odoo import models, fields
from datetime import datetime


class BilalProducts(models.Model):
    _name = "bilal.products"
    _rec_name = "product_name"

    product_name = fields.Char(string="Name")
    product_price = fields.Integer(string="Price/Unit")
    product_description = fields.Char(string="Product Description")
    purchase_date = fields.Date(string="Date", default=datetime.today())
    # product_code = fields.Integer(string="Code")


