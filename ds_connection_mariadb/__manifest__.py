# -*- coding: utf-8 -*-
{
    'name': "ASB Connection MariaDB",

    'summary': """
        Beberapa hal yang harus diperhatikan adalah :
        1. Database MariaDB sudah dibuat terlebih dahulu
        2. Membuat Parameter yang akan menampung value connection
        3. Agar lebih memudahkan, connection ini dibuat di dalam Function
        4. Ketika ingin menggunakan connection, cukup panggil nama Function nya""",

    'description': """
        Membuat Koneksi Database dari MariaDB ke Odoo
    """,

    'author': "Arkana Solusi Bisnis",
    'website': "http://www.arkana.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/list_city.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
