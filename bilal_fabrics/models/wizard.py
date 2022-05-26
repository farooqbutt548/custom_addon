from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'bilal.wizard'
    _description = 'Wizard description here'


    product_id = fields.Many2one('bilal.products', string='Add Produccts', required=True)
    attendee_ids = fields.Many2many('res.partner', string='Attendee')
