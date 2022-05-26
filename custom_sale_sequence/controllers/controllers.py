# -*- coding: utf-8 -*-
# from odoo import http


# class CustomSaleSequence(http.Controller):
#     @http.route('/custom_sale_sequence/custom_sale_sequence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_sale_sequence/custom_sale_sequence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_sale_sequence.listing', {
#             'root': '/custom_sale_sequence/custom_sale_sequence',
#             'objects': http.request.env['custom_sale_sequence.custom_sale_sequence'].search([]),
#         })

#     @http.route('/custom_sale_sequence/custom_sale_sequence/objects/<model("custom_sale_sequence.custom_sale_sequence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_sale_sequence.object', {
#             'object': obj
#         })
