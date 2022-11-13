ticket_to_france = 150
profit_margin = 1.40
items_collection = input().split("|")
budget = float(input())

max_clothes_price = 50.00
max_shoes_price = 35.00
max_accessories_price = 20.50
total_profit = 0
enough_budget = False

for items in items_collection:

    current_item, current_value = items.split("->")
    current_value = float(current_value)
    if \
            current_item == "Clothes" and current_value <= max_clothes_price or \
                    current_item == "Shoes" and current_value <= max_shoes_price or \
                    current_item == "Accessories" and current_value <= max_accessories_price:
        if current_value <= budget:
            budget -= current_value
            item_profit = current_value * profit_margin
            budget += item_profit
            total_profit += current_value * 0.4
            print(f"{item_profit:.2f}", end=" ")
            if budget >= ticket_to_france:
                enough_budget = True
                break
print()
print(f"Profit: {total_profit:.2f}")
if not enough_budget:
    print("Not enough money.")
else:
    print("Hello, France!")
