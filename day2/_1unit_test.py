"""
Processes a list of orders and calculates the total price.
Each order contains multiple items. Each item is a dictionary with 'name', 'quantity', 'price', and 'discount'.
Handles edge cases such as missing fields, negative values, and invalid discounts.
"""

import unittest

def process_orders(orders):
    total_price = 0
    total_items = 0

    for order in orders:
        for item in order.get('items', []):
            name = item.get('name', '')
            quantity = item.get('quantity', 0)
            price = item.get('price', 0)
            discount = item.get('discount', 0)

            # Edge case handling: Skip items with invalid or negative values
            if quantity <= 0 or price <= 0 or discount < 0 or discount > 100:
                continue

            # Calculate price after discount
            item_price = quantity * price * (1 - discount / 100)
            total_price += item_price
            total_items += quantity

    # Apply bulk discount if total items exceed 100
    if total_items > 100:
        total_price *= 0.95  # Apply a 5% discount

    return total_price

class TestProcessOrders(unittest.TestCase):
    def test_normal_orders(self):
        orders = [
            {'items': [{'name': 'Apple', 'quantity': 2, 'price': 1.0, 'discount': 10},
                       {'name': 'Banana', 'quantity': 3, 'price': 0.5, 'discount': 5}]},
            {'items': [{'name': 'Orange', 'quantity': 1, 'price': 0.75, 'discount': 0}]}
        ]
        self.assertAlmostEqual(int(process_orders(orders)), 3)

    def test_invalid_data(self):
        orders = [
            {'items': [{'name': 'Apple', 'quantity': -2, 'price': 1.0, 'discount': 10}]}
        ]
        self.assertAlmostEqual(process_orders(orders), 0)

    def test_bulk_discount(self):
        orders = [
            {'items': [{'name': 'Apple', 'quantity': 60, 'price': 1.0, 'discount': 0},
                       {'name': 'Banana', 'quantity': 50, 'price': 0.5, 'discount': 0}]}
        ]
        self.assertAlmostEqual(process_orders(orders), 80.75)

    def test_empty_orders(self):
        orders = []
        self.assertAlmostEqual(process_orders(orders), 0)

    def test_missing_fields(self):
        orders = [
            {'items': [{'name': 'Apple', 'price': 1.0, 'discount': 10}]}
        ]
        self.assertAlmostEqual(process_orders(orders), 0)

    def test_large_numbers(self):
        orders = [
            {'items': [{'name': 'Apple', 'quantity': 1000, 'price': 0.1, 'discount': 5}]}
        ]
        self.assertAlmostEqual(process_orders(orders), 90.25)

if __name__ == "__main__":
    print("Unit Test[1]")

    unittest.main()