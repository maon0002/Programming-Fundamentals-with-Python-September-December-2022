lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0

for time in range(1, lost_fights + 1):

    if time % 2 == 0:
        expenses += helmet_price
    if time % 3 == 0:
        expenses += sword_price
        if time % 2 == 0:
            expenses += shield_price
    if time % 12 == 0:
        expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
