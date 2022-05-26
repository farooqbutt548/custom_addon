# -*- coding: utf-8 -*-
# from odoo import http


# class Fabrics(http.Controller):
#     @http.route('/fabrics/fabrics/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fabrics/fabrics/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fabrics.listing', {
#             'root': '/fabrics/fabrics',
#             'objects': http.request.env['fabrics.fabrics'].search([]),
#         })

#     @http.route('/fabrics/fabrics/objects/<model("fabrics.fabrics"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fabrics.object', {
#             'object': obj
#         })
