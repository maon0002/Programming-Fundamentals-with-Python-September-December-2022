menu_dict = {}
while True:
    string_input = input()
    if string_input == "buy":
        break
    item, price, qty = string_input.split()
    if item not in menu_dict.keys():
        menu_dict[item] = [0, 0]
    menu_dict[item][0] = float(price)
    menu_dict[item][1] += int(qty)

for product_name, profit in menu_dict.items():
    print(f"{product_name} -> {profit[0] * profit[1]:.2f}")
