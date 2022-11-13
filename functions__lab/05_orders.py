def order_calculation(product: str, quantity: int):
    coffee_price = 1.50
    water_price = 1.00
    coke_price = 1.40
    snacks_price = 2.00
    total_cost = 0
    if product == "coffee":
        total_cost = quantity * coffee_price
    elif product == "water":
        total_cost = quantity * water_price
    elif product == "coke":
        total_cost = quantity * coke_price
    elif product == "snacks":
        total_cost = quantity * snacks_price
    return f"{total_cost:.2f}"


product_input = input()
qty_input = int(input())
print(order_calculation(product_input, qty_input))
