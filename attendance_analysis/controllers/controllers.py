# -*- coding: utf-8 -*-
# from odoo import http


# class AttendanceAnalysis(http.Controller):
#     @http.route('/attendance_analysis/attendance_analysis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/attendance_analysis/attendance_analysis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('attendance_analysis.listing', {
#             'root': '/attendance_analysis/attendance_analysis',
#             'objects': http.request.env['attendance_analysis.attendance_analysis'].search([]),
#         })

#     @http.route('/attendance_analysis/attendance_analysis/objects/<model("attendance_analysis.attendance_analysis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('attendance_analysis.object', {
#             'object': obj
#         })
