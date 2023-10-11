from unittest.mock import patch
from before import Authorizer_SMS

class TestAuthorizer:

    def test_generate_sms_code(self):
        a = Authorizer_SMS()
        a.generate_sms_code()
        assert len(a.code) == 6
        assert type(a.code) == str
    
    @patch("builtins.input")
    def test_authorize_success(self, patch_input):
        a = Authorizer_SMS()
        a.generate_sms_code()
        patch_input.return_value = a.code
        a.authorize()
        assert a.authorized == True
        