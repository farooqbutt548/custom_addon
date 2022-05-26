# -*- coding: utf-8 -*-
# from odoo import http


# class RadicalAcademy(http.Controller):
#     @http.route('/radical_academy/radical_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/radical_academy/radical_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('radical_academy.listing', {
#             'root': '/radical_academy/radical_academy',
#             'objects': http.request.env['radical_academy.radical_academy'].search([]),
#         })

#     @http.route('/radical_academy/radical_academy/objects/<model("radical_academy.radical_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('radical_academy.object', {
#             'object': obj
#         })
