# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ds_connection_mariadb(models.Model):
#     _name = 'ds_connection_mariadb.ds_connection_mariadb'
#     _description = 'ds_connection_mariadb.ds_connection_mariadb'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
