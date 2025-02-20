"""
1. Small Fruit Shop Change Calculator  (7.pt)

Implement `fruit_shop_change(budget_krw, fruits_order)` function that calculates the change in Japanese Yen (JPY) after purchasing fruits.
"""

 # 1.
def fruit_shop_change(budget_krw, fruits_order):
    """
    Calculate the change in Japanese Yen (JPY) after purchasing fruits.

    :param budget_krw: A float representing the budget in KRW. (int/float)
    :param fruits_order: A dictionary of fruit names and quantities. (dict[str, int])
    :return: A string representing the change or an error message. (str)
    """
    prices_krw = {"apple": 1000, "banana": 1500, "orange": 800}

    if isinstance(budget_krw, (int,float)) or isinstance(fruits_order, dict) :
        order_fruits = list(fruits_order.keys())

        order_cost = {}
        for order_fruit in order_fruits :
            price = prices_krw[order_fruit]
            quantity = fruits_order[order_fruit]
            order_cost[order_fruit] = price * quantity

        total_cost = sum(order_cost.values())
        change = budget_krw - total_cost
        change_JPY = round(change/9.5, 2)
        if budget_krw < total_cost :
            return 'Insufficient budget.'
        else :
            return f'Your change is {change_JPY} JPY.'
    else : 
        return 'Invalid input'

print(fruit_shop_change(10000, {'apple' :3, 'banana': 2}))
print(fruit_shop_change(2000, {'apple' : 2, 'orange' : 1}))
print(fruit_shop_change('hi', 2))