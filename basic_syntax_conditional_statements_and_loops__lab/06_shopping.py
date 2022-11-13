budget = int(input())
input_line = input()
purchases = 0
is_budget_enough = True

while input_line != "End":
    product_price = int(input_line)
    purchases += product_price
    if purchases > budget:
        is_budget_enough = False
        break
    input_line = input()

if is_budget_enough:
    print("You bought everything needed.")
else:
    print("You went in overdraft!")
