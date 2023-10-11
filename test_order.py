from before import Order

class TestOrder:

    def test_init_order(self):
        o = Order()
        assert o.status == "open"
    
    def test_set_status(self):
        o = Order()
        o.set_status("blocked")
        assert o.status == "blocked"

