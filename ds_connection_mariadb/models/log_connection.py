from odoo import models, fields, api, _
from odoo.exceptions import UserError
import mariadb, logging

class LogConnection(models.Model):
    _name = 'log.connection'
    _description = 'Connection MariaDB'

    name = fields.Char(string='Name')

    def _get_authentication(self):

        conn = mariadb.connect(
            user = 'admin',
            password = 'arkana',
            port = 3306,
            host = 'localhost',
            database = 'sharing_session',
        )
        
        # Sharing Session 1
        return conn.cursor(), conn
        # Sharing Session 2
        # return conn.cursor(dictionary=True), conn
    
