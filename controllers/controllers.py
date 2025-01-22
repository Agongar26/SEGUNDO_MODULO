# -*- coding: utf-8 -*-
# from odoo import http


# class SegundoModulo(http.Controller):
#     @http.route('/segundo__modulo/segundo__modulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/segundo__modulo/segundo__modulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('segundo__modulo.listing', {
#             'root': '/segundo__modulo/segundo__modulo',
#             'objects': http.request.env['segundo__modulo.segundo__modulo'].search([]),
#         })

#     @http.route('/segundo__modulo/segundo__modulo/objects/<model("segundo__modulo.segundo__modulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('segundo__modulo.object', {
#             'object': obj
#         })

