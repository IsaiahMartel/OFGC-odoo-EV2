# -*- coding: utf-8 -*-
# from odoo import http


# class Ofgc(http.Controller):
#     @http.route('/ofgc/ofgc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ofgc/ofgc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ofgc.listing', {
#             'root': '/ofgc/ofgc',
#             'objects': http.request.env['ofgc.ofgc'].search([]),
#         })

#     @http.route('/ofgc/ofgc/objects/<model("ofgc.ofgc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ofgc.object', {
#             'object': obj
#         })
