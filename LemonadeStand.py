# Author
# GitHub username: Aline_Lima
# Date: 01/16/2023
# Description: Creates classes and methods for recording the menu items, cost,
# daily sales, and profits of a lemonade stand.

class InvalidSalesItemError(Exception):
    pass


class MenuItem:
    """Creates a Menu Item method which includes name, cost of the product and the selling price."""

    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        return self.name

    """This method gets the name of the item and returns it"""

    def get_wholesale_cost(self):
        return self.wholesale_cost

    """This method gets the whole sale cost and returns it"""

    def get_selling_price(self):
        return self.selling_price

    """This method gets the selling price and returns it"""


class SalesForDay:
    """A class that stores all sales made in a day"""

    def __init__(self, day, sales_dict):
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        return self.day

    """returns day"""

    def get_sales_dict(self):
        return self.sales_dict

    """return sales dictionary """


class LemonadeStand:
    def __init__(self, name):
        """
        A class named Lemonade Stand which includes name, day, menu items, the sales for the day, items to be added, sales of each menu item in a day
        """
        self._name = name
        self._current_day = 0
        self._menu_items = {}
        self._sales_for_day_list = []

    def get_name(self):
        return self.name

    """get stand name and returns it"""

    def add_menu_items(self, item):
        self._menu_items[item.get_name] = item

    """add menu items """

    def enter_sales_for_today(self, items_sold):
        """check for items sold if they are in the dictionary """
        temp_dict = dict()  # check for each item in items_sold to make sure they are valid
        for item in items_sold.keys():
            if item in self._menu_items:
                temp_dict[item] = items_sold[item]
            else:
                raise InvalidSalesItemError
        # once done finding all valid items, add to class list#
        self._sales_for_day_list.append(SalesForDay(self._current_day, temp_dict))
        self._current_day += 1

    def get_sales_dict_for_day(self, day):
        """Takes as a parameter a dictionary where the keys are names of items sold """
        output = self._sales_for_day_list[day]
        return output.get_sales_dict()

    def total_sales_for_menu_item(self, name_of_menu_item):
        """Returns the number of that item sold on that day"""
        sales_number = 0
        for sales in self._sales_for_day_list:
            if name_of_menu_item in sales.keys():
                sales_number += sales[name_of_menu_item]

        return sales_number

    def CalculateProfit(self, itemName, numItems):
        """calculates profit"""
        item = self._menu_items[itemName]
        profit = item.selling_price - self.wholesale_price
        return numItems * profit

    def total_profit_for_menu_item(self, product):
        """gets and returns total profit for item"""
        # product is the name of the item in question#
        profit = 0

        for day in self._sales_for_day:
            tempDict = day.get_sales_dict()
            if (product in tempDict.keys()):
                profit += tempDict[product]

            # if sales only contains the number of each item sold, will need to multiple profit by the price of the item
                return CalculateProfit(product, profit)

    def total_profit_for_stand(self):
        """gets and returns total profit for stand"""
        allItems = {}
        for day in self._sale_for_day:
            tempDict = day.get_sales_dict()

        for item in tempDict.keys():
            if item in allItems:
                allItems[item] += tempDict[item]
            else:
                allItems[item] = tempDict[item]

        # find the profit of every single item

        profit = 0
        for item in allItems.keys():
            profit += self.CalculateProfit(item, allItems[item])

        return profit


