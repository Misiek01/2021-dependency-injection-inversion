import pytest
from before import Order, Authorizer_SMS
from unittest.mock import patch

class TestOrder:

    def test_order_status_init(self):
        order = Order()
        assert order.status == "open"

    def test_order_set_status_changes(self):
        order = Order()
        order.set_status("paid")
        assert order.status == "paid"



class TestAuthorizer_SMS:

    def test_init_authorized(self):
        auth = Authorizer_SMS()
        auth.is_authorized == False

    def test_code_string_isdecimal(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        auth.code.isdecimal() == True

    def test_authorize_success(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        with patch('builtins.input', return_value=auth.code):
            auth.authorize()
            assert auth.is_authorized() == True

    @patch('builtins.input', return_value="1234567")
    def test_authorize_fail(self, mocked_input):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        auth.authorize()
        assert auth.is_authorized() == False


class TestPaymentProcessor:

    def test_payment_success(self):
        # ???
        assert True

    def test_payment_fail(self):
        # ???
        assert True