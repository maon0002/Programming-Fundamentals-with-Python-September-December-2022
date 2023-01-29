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
