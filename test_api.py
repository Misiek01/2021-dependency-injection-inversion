from unittest.mock import patch
from utils import OrderInterface

@patch("utils.api_get_data_from_db", return_value = {"ids": [1,5]})
def test_get_ids(patched_data):
    o = OrderInterface()
    ids = o.get_ids()
    assert ids == [1,5]