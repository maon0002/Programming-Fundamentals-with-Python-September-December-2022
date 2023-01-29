# import re
#
# input_line = input()
# initial_demons = input_line.split(", ")
# demons_name_pattern = r'([ ,])'
# demons = []
# for i in range(len(initial_demons)):
#     if not re.findall(demons_name_pattern, initial_demons[i]) and len(initial_demons[i]) > 0:
#         demons.append(initial_demons[i])
# sorted_demons = sorted(demons, key=lambda x: x)
#
# for i in range(len(sorted_demons)):
#     name = sorted_demons[i]
#     health_pattern = r'[^0-9\+\-\*\/\.,]+'
#     health_matches = re.findall(health_pattern, name)
#     total_health = 0
#     for char in health_matches:
#         current_char_value = ord(char)
#         total_health += current_char_value
#     damage = 0
#     damage_pattern = r'([\-]*[0-9]+[\.]*[\d]+|\d+)'
#     # damage_pattern_divide_multiply = r'([\*\/]+)'
#     damage_pattern_divide_multiply = r'[\*\/]'
#     damage_matches = re.findall(damage_pattern, name)
#     damage_extra_matches = re.findall(damage_pattern_divide_multiply, name)
#     damage_subtotal = sum(float(digit) for digit in damage_matches)
#     damage += damage_subtotal
#     if damage_extra_matches:
#         if "*" in damage_extra_matches:
#             multiply_times = damage_extra_matches.count("*") * 2
#             damage *= multiply_times
#         if "/" in damage_extra_matches:
#             divide_times = damage_extra_matches.count("/") * 2
#             damage /= divide_times
#     print(f"{name} - {total_health} health, {damage:.2f} damage")


import re

input_line = input()
initial_demons = input_line.split(", ")
demons_name_pattern = r'([ ,])'
demons = []
for i in range(len(initial_demons)):
    if not re.findall(demons_name_pattern, initial_demons[i]) and len(initial_demons[i]) > 0:
        demons.append(initial_demons[i])
sorted_demons = sorted(demons, key=lambda x: x)

for i in range(len(sorted_demons)):
    name = sorted_demons[i]
    health_pattern = r'([^0-9\+\-\*\/\.])'
    health_matches = re.findall(health_pattern, name)
    total_health = 0
    for char in health_matches:
        current_char_value = ord(char)
        total_health += current_char_value
    damage = 0
    damage_pattern = r'([\-]*[0-9]+[\.]*[\d]+|\d+)'
    # damage_pattern_divide_multiply = r'([\*\/]+)'
    damage_pattern_divide_multiply = r'[\*\/]'
    damage_matches = re.findall(damage_pattern, name)
    damage_extra_matches = re.findall(damage_pattern_divide_multiply, name)

    if damage_extra_matches:
        extra_pattern = r'([\-]*[0-9]+[\.]*[\d]+|\d+|[\*\/])'
        extra_matches = re.findall(extra_pattern, name)
        extra_calc = 0
        for value in extra_matches:
            if value == "*" or value == "/":
                if value == "*":
                    extra_calc = extra_calc * 2
                elif value == "/":
                    extra_calc = extra_calc / 2
            else:
                extra_calc += float(value)
        damage = extra_calc
    else:
        damage_subtotal = sum(float(digit) for digit in damage_matches)
        damage += damage_subtotal
    print(f"{name} - {total_health} health, {damage:.2f} damage")

    # if damage_extra_matches:
    #     if "*" in damage_extra_matches:
    #         multiply_times = damage_extra_matches.count("*") * 2
    #         damage *= multiply_times
    #     if "/" in damage_extra_matches:
    #         divide_times = damage_extra_matches.count("/") * 2
    #         damage /= divide_times
