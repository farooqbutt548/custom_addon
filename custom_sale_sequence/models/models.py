# -*- coding: utf-8 -*-
##############################################################################
#
#    Global Creative Concepts Tech Co Ltd.
#    Copyright (C) 2018-TODAY iWesabe (<http://www.iwesabe.com>).
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import api, fields, models

class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"
    # _order = "order_id, sl_no,id"

    sequence = fields.Integer(string='Sequence', default=1)
    sl_no = fields.Integer(compute='_sequence_ref', store=True)

    @api.depends('order_id.order_line.product_id')
    def _sequence_ref(self):
        no = 0
        for line in self.order_id.order_line.sorted('sequence'):
            if line.display_type==False:
                no += 1
                line.update({'sl_no':no})