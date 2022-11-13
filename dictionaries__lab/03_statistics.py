input_string = input()
statistic_dict = {}

while input_string != "statistics":
    product, qty = input_string.split(": ")
    if product not in statistic_dict.keys():
        statistic_dict[product] = 0
    statistic_dict[product] += int(qty)

    input_string = input()

print("Products in stock:")

for product, qty in statistic_dict.items():
    print(f"- {product}: {qty}")
print(f"Total Products: {len(statistic_dict)}\nTotal Quantity: {sum(statistic_dict.values())}")
