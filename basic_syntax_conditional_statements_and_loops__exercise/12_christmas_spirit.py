decorations_qty = int(input())
days_left_until_xmas = int(input())

total_cost = 0
total_spirit = 0

# price set
ornaments_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

# points_set
ornaments_set_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17
cat_mess_substr = 20
extra_spirit_points = 30

for day in range(1, days_left_until_xmas + 1):
    if day % 11 == 0:
        decorations_qty += 2
    if day % 2 == 0:
        total_cost += ornaments_set * decorations_qty
        total_spirit += ornaments_set_points
    if day % 3 == 0:
        total_cost += (tree_garland * decorations_qty) + (tree_skirt * decorations_qty)
        total_spirit += tree_skirt_points + tree_garland_points
    if day % 5 == 0:
        total_cost += tree_lights * decorations_qty
        total_spirit += tree_lights_points
        if day % 3 == 0:
            total_spirit += extra_spirit_points
    if day % 10 == 0:
        total_spirit -= cat_mess_substr
        total_cost += tree_skirt + tree_garland + tree_lights

if days_left_until_xmas == 10:
    total_spirit -= extra_spirit_points

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
