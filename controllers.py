# -*- coding: utf-8 -*-
from openerp import http

class OnlineStore(http.Controller):
    @http.route('/store', auth='public', website=True)
    def index(self, **kw):
        # Products = http.request.env['product.template']
        return http.request.render('online_store.index', {
            # 'products': Products.search([])
        })

    @http.route('/simple', auth='public', website=True)
    def page(self, **kw):
        # Products = http.request.env['product.template']
        return http.request.render('online_store.page', {
            # 'products': Products.search([])
        })

    @http.route('/login1', auth='public', website=True)
    def login(self, **kw):
        return http.request.render('online_store.login_form1', {
        })