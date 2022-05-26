# -*- coding: utf-8 -*-
# from odoo import http


# class BilalFabrics(http.Controller):
#     @http.route('/bilal_fabrics/bilal_fabrics/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bilal_fabrics/bilal_fabrics/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bilal_fabrics.listing', {
#             'root': '/bilal_fabrics/bilal_fabrics',
#             'objects': http.request.env['bilal_fabrics.bilal_fabrics'].search([]),
#         })

#     @http.route('/bilal_fabrics/bilal_fabrics/objects/<model("bilal_fabrics.bilal_fabrics"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bilal_fabrics.object', {
#             'object': obj
#         })
