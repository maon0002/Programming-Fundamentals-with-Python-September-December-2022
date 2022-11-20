#     5. Furniture
# Write a program that calculates the total cost of bought furniture.
# You will be given information about each purchase on separate lines until you receive the command "Purchase".
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}".
# The price could be a floating-point or integer number.
# You should store the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"


import re

pattern = r'(>>([A-Za-z]+)<<([\d\.]+)!(\d+))'
input_line = input()

total_money_spend = 0
print("Bought furniture:")
while input_line != "Purchase":
    output_line = re.search(pattern, input_line)
    if output_line:
        check, furniture_name, price, quantity = output_line.groups()
        print(furniture_name)
        total_money_spend += int(quantity) * float(price)
    input_line = input()


print(f"Total money spend: {total_money_spend:.2f}")
