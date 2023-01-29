import re

command = input()
total_income = 0

while command != "end of shift":
    pattern = r'^[^\|\$\%\.]*%([A-Z][a-z]+)%[^\|\$\%\.]*<(\w+)>[^\|\$\%\.]*\|(\d+)[^\|\$\%\.]*\|[^\|\$\%\.\d]*(\d+\.*[0-9]+)\$$'
    if re.match(pattern, command):
        customer, product, count, price = re.match(pattern, command).groups()
        # print(customer, product, count, price)
        # print(re.match(pattern, command).groups())
        subtotal = int(count) * float(price)
        total_income += subtotal
        print(f"{customer}: {product} - {subtotal:.2f}")

    command = input()

print(f"Total income: {total_income:.2f}")
