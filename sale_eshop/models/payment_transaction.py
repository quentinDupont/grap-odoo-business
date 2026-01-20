# Copyright (C) 2026 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class PaymentTransaction(models.Model):
    _inherit = "payment.transaction"

    """
	This code override Mollie's code to check if the sale
	come from sale_eshop → it adds a param in URL that will be
	catch by MollieController /payment/mollie/return in function
	mollie_return_from_checkout → so we can redirect to website sale_eshop
	instead of Odoo
	"""

    def _mollie_prepare_payment_payload(self, api_type):
        print("=== override sale_eshop Mollie")

        payment_data, params = super()._mollie_prepare_payment_payload(api_type)

        if api_type == "order" and self.sale_order_ids:
            order = self.sale_order_ids[0]
            if order.eshop_sale:
                base_url = payment_data.get("redirectUrl")
                payment_data["redirectUrl"] = f"{base_url}&eshop_sale=1"

        return payment_data, params
