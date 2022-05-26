# -*- coding: utf-8 -*-
# from odoo import http


# class HammaadCustom(http.Controller):
#     @http.route('/hammaad_custom/hammaad_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hammaad_custom/hammaad_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hammaad_custom.listing', {
#             'root': '/hammaad_custom/hammaad_custom',
#             'objects': http.request.env['hammaad_custom.hammaad_custom'].search([]),
#         })

#     @http.route('/hammaad_custom/hammaad_custom/objects/<model("hammaad_custom.hammaad_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hammaad_custom.object', {
#             'object': obj
#         })
