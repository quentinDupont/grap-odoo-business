# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request

from odoo.addons.payment.controllers.post_processing import PaymentPostProcessing


class SaleEshopPaymentPostProcessing(PaymentPostProcessing):

    """
    Inherit Odoo Payment Controller to redirect Mollie payment to sale_eshop website
    """

    @http.route(
        "/payment/status", type="http", auth="public", website=True, sitemap=False
    )
    def display_status(self, **kwargs):
        super().display_status()
        sale_eshop = kwargs.get("sale_eshop") == "1"
        import pdb

        pdb.set_trace()
        if sale_eshop:
            print("ouais ouaaaaaaaaaaaais dans sale_eshop")
            return request.redirect("http://127.0.0.1:8080", local=False)
