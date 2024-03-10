def cost_calculator(*pizzas,drinks = [], wings =[], coupon = 0):
    keyDrinks = {"small": 2.00, "medium": 3.00, "large": 3.5, "tub": 3.75}
    keyWings = {10: 5, 20: 9, 40: 17.5, 100: 48}
    keyToppings = {"pepperoni": 1, "mushroom": 0.5, "olive": 0.5, "anchovy": 2, "ham": 1.5}
    total = 0
    for pizza in pizzas:
        total += 13
        for topping in pizza:
            total += keyToppings[topping]
    for drink in drinks:
        total += keyDrinks[drink]
    for wing in wings:
        total += keyWings[wing]
    total += total * 0.0625
    total -= total * coupon
    return total
