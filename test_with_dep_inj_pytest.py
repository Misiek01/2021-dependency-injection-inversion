import pytest
from with_dep_inj import Order, Authorizer_SMS, PaymentProcessor
from unittest.mock import patch

class TestPaymentProcessor:

    def test_init(self):
        auth = Authorizer_SMS()
        p = PaymentProcessor(auth)
        assert p.authorizer == auth

    def test_payment_success(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        with patch('builtins.input', return_value=auth.code):
            p = PaymentProcessor(auth)
            order = Order()
            p.pay(order)
            assert order.status == "paid"

    def test_payment_fail(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        with patch('builtins.input', return_value="1234567"):
            p = PaymentProcessor(auth)
            order = Order()
            with pytest.raises(Exception):
                p.pay(order)
