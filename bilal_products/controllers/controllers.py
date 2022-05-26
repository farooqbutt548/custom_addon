# -*- coding: utf-8 -*-
# from odoo import http


# class BilalProducts(http.Controller):
#     @http.route('/bilal_products/bilal_products/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bilal_products/bilal_products/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bilal_products.listing', {
#             'root': '/bilal_products/bilal_products',
#             'objects': http.request.env['bilal_products.bilal_products'].search([]),
#         })

#     @http.route('/bilal_products/bilal_products/objects/<model("bilal_products.bilal_products"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bilal_products.object', {
#             'object': obj
#         })
