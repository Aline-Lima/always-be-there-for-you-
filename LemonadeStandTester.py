import LemonadeStand

class TestLemonadeStand:
    """unit tests for LemonadeStand.py"""
    def setUp(self):
        #creates an instance of the object for each test
        stand = LemonadeStand("Bob's Lemonade")

    def best_get_name(self):
        #make sure name is stored properly
        assertEquals(stand.getName(), "Bob's Lemonade")

    def test_add_menu_item(self):
        #make sure items can be added to menu
        stand.add_menu_item(Item("pizza",2, 5))
        assertEquals(len(stand.get_menu_item()),1)

    def test_total_profit_for_menu_item(self):
        # assume 5 pizzas where sold total
        self.Equals(stand.total_profit_for_menu_item("pizza"), 15)
        self.assertFalse('0'.isupper())

    def test_total_profit_for_menu_item_fail(self):
        # assume 5 pizzas where sold total
        self.Equals(stand.total_profit_for_menu_item("pizza"), 0)