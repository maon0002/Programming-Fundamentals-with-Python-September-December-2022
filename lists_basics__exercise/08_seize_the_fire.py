fires_with_their_cells = input().split(" = ")
water = int(input())
simple_values_list = "#".join(fires_with_their_cells)

simple_values_list = simple_values_list.split("#")
high_fire_range = range(81, 125)
medium_fire_range = range(51, 80)
low_fire_range = range(1, 50)
effort = 0.0
total_fire = 0
is_end = False
print("Cells:")
counter = 0

for validity in range(0, len(simple_values_list), 2):
    # current_value = 0
    # current_cell = ""

    current_cell = simple_values_list[validity]
    current_value = int(simple_values_list[validity + 1])

    if (current_cell == "High" and current_value in high_fire_range) or \
            (current_cell == "Medium" and current_value in medium_fire_range) or \
            (current_cell == "Low" and current_value in low_fire_range):
        if water > current_value:
            water -= current_value
            effort += current_value * 0.25
            total_fire += current_value
            print(f" - {current_value}")
        else:
            break
    else:
        continue
    is_end = True

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
