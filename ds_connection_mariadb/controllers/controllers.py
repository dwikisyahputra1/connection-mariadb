# -*- coding: utf-8 -*-
# from odoo import http


# class DsConnectionMariadb(http.Controller):
#     @http.route('/ds_connection_mariadb/ds_connection_mariadb/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ds_connection_mariadb/ds_connection_mariadb/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ds_connection_mariadb.listing', {
#             'root': '/ds_connection_mariadb/ds_connection_mariadb',
#             'objects': http.request.env['ds_connection_mariadb.ds_connection_mariadb'].search([]),
#         })

#     @http.route('/ds_connection_mariadb/ds_connection_mariadb/objects/<model("ds_connection_mariadb.ds_connection_mariadb"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ds_connection_mariadb.object', {
#             'object': obj
#         })
