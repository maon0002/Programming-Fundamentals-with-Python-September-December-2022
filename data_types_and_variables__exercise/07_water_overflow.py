number_of_lines = int(input())
tank_capacity = 255
added_water = 0

for x in range(number_of_lines):
    water_litters = int(input())  # 1000, 250, 20

    if added_water + water_litters > tank_capacity:
        print("Insufficient capacity!")
    elif added_water + water_litters <= tank_capacity:
        added_water += water_litters

print(added_water)
