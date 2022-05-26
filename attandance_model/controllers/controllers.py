# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request

class Attendanceportal(http.Controller):
    @http.route('/attandance_model', auth='public', website=True)
    def list(self, **kw):
        return http.request.render('attandance_model.leave_portal', {})
# return http.request.render('website.page_main_use_case',
#                          {'projects': ''})

# class AttandanceModel(http.Controller):
#     @http.route('/attandance_model/attandance_model/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"
#
#     @http.route('/attandance_model/attandance_model/objects/', auth='public', website='true')
#     def list(self, **kw):
#         return http.request.render('attandance_model.listing', {
#             'root': '/attandance_model/attandance_model',
#             'objects': http.request.env['attandance_model.attandance_model'].search([]),
#         })
#
#     @http.route('/attandance_model/attandance_model/objects/<model("attandance_model.attandance_model"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('attandance_model.object', {
#             'object': obj
#         })
