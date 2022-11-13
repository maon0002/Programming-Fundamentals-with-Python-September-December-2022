budget = float(input())
kg_flour_price = float(input())
eggs_pack_price = kg_flour_price * 0.75
quarter_milk_price = (kg_flour_price * 1.25) / 4
recipe = kg_flour_price + eggs_pack_price + quarter_milk_price
colored_eggs = 0
current_bread_count = 0

while budget >= recipe:
    budget -= recipe
    current_bread_count += 1
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs -= (current_bread_count - 2)

print(
    f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
