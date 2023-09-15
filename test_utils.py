from unittest.mock import patch
from utils import OrderInterface

@patch("utils.api_get_data_from_db", return_value = {"ids":[1,2,3]})
def test_get_ids(data_mock):
    order_itf = OrderInterface()
    ids = order_itf.get_ids()
    assert ids == [1,2,3]


def test_get_ids_context_manager():
    with patch("utils.api_get_data_from_db") as db:
        db.return_value = {"ids":[1,2,3]}
        order_itf = OrderInterface()
        ids = order_itf.get_ids()
        db.return_value = {"ids":[5,6,7]}
        ids = order_itf.get_ids()
        assert ids == [5,6,7]