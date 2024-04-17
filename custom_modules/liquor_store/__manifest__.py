# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'liquor_store',
    'depends' : ['mail', 'base', 'web', 'sale', 'board'],
    'data': [
        'security/access_groups.xml',
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'data/sequence_data.xml',
        'views/liquor_store_brand.xml',
        'views/liquor_store_bottles.xml',
        'views/liquor_store_bottle_size.xml',
        'views/liquor_store_customer.xml',
        'views/liquor_store_supplier.xml',
        'views/liquor_store_rfq.xml',
        'views/liquor_store_invoices.xml',
        'views/liquor_store_sales.xml',
        'views/liquor_store_sales_order_reporting.xml',
        'views/liquor_store_sales_analysis.xml',
        'views/liquor_store_sales_payment_type_analysis.xml',
        'views/liquor_store_supplier_transaction.xml',
        'views/sales_dashboard.xml',
        'views/liquor_store_menus.xml',
        'reports/sales_orders_report_template.xml',
        'reports/report.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'liquor_store/static/src/components/**/*.js',
            'liquor_store/static/src/components/**/*.xml',
            'liquor_store/static/src/components/**/*.scss',
            'liquor_store/static/src/**/*',
        ],
    },
}