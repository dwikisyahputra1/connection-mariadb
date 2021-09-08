from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging, mariadb

class ListCity(models.Model):
    _name = 'list.city'
    _description = 'List City'

    name = fields.Char(string='City')
    
    def connection_mariadb(self):
        cursor, conn = self.env['log.connection']._get_authentication()

        # Cara 1 - Tidak menggunakan penjagaan di query nya
        query = """SELECT id, name FROM shases_city"""
        cursor.execute(query)

        # Cara 2 - Menggunakan Penjagaan di query nya (sebenernya fungsi ini dibi)
        # try:
        #     query = """SELECT ids, name FROM shases_city"""
        #     cursor.execute(query)
        # except mariadb.Error as a:
        #     logging.error('Except {%s}' % a)

        data = cursor.fetchall()
        
        conn.close()