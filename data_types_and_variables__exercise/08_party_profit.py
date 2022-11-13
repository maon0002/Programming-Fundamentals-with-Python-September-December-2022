group_size = int(input())
days = int(input())
current_profit = 0
current_expenses = 0
for day in range(1, days + 1):
    profit_per_day = 50
    current_profit += profit_per_day
    if day % 15 == 0:
        group_size += 5
    if day % 10 == 0:
        group_size -= 2
    if day % 3 == 0:
        motivational_party = 3 * group_size
        current_expenses += motivational_party
    if day % 5 == 0:
        current_profit += 20 * group_size
        if day % 3 == 0:
            current_expenses += 2 * group_size

    food_expenses_per_person = 2 * group_size
    current_expenses += food_expenses_per_person

diff = current_profit - current_expenses
profit_share = int(diff / group_size)
print(f"{group_size} companions received {profit_share} coins each.")
