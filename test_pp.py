from unittest.mock import patch

import pytest
from with_dep_inj import Order, Authorizer_SMS, PaymentProcessor


class TestPaymentProcessor:

    @patch("builtins.input")
    def test_payment_success(self, patch_input):
        a = Authorizer_SMS()
        a.generate_sms_code()
        patch_input.return_value = a.code
        p = PaymentProcessor(authorizer=a)
        order = Order()
        p.pay(order)
        assert order.status == "paid"

    @patch("builtins.input")
    def test_payment_fail(self, patch_input):
        a = Authorizer_SMS()
        a.generate_sms_code()
        patch_input.return_value = "abc"
        p = PaymentProcessor(authorizer=a)
        order = Order()

        with pytest.raises(Exception):
            p.pay(order)


