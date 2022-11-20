#     4. Nether Realms
# Mighty battle is coming. In the stormy nether realms, demons are fighting against each other for supremacy in a duel from which only one will survive.
# Your job, however is not so exciting. You are assigned to sign in all the participants in the nether realm's mighty battle's demon book, which of course is sorted alphabetically.
# A demon's name contains his health and his damage.
# The sum of the asci codes of all characters (excluding numbers (0-9), arithmetic symbols ('+', '-', '*', '/') and delimiter dot ('.')) gives a demon's total health.
# The sum of all numbers in his name forms his base damage. Note that you should consider the plus '+' and minus '-' signs (e.g. +10 is 10 and -10 is -10). However, there are some symbols ('*' and '/') that can further alter the base damage by multiplying or dividing it by 2 (e.g. in the name "m15*/c-5.0", the base damage is 15 + (-5.0) = 10 and then you need to multiply it by 2 (e.g. 10 * 2 = 20) and then divide it by 2 (e.g. 20 / 2 = 10)).
# So, multiplication and division are applied only after all numbers are included in the calculation and in the order they appear in the name.
# You will get all demons on a single line, separated by commas and zero or more blank spaces. Sort them in alphabetical order and print their names along their health and damage.
# Input
# The input will be read from the console. The input consists of a single line containing all demon names separated by commas and zero or more spaces in the format: "{demon name}, {demon name}, … {demon name}"
# Output
# Print all demons sorted by their name in ascending order, each on a separate line in the format:
#     • "{demon name} - {health points} health, {damage points} damage"
# Constraints
#     • A demon's name will contain at least one character
#     • A demon's name cannot contain blank spaces ' ' or commas ','
#     • A floating point number will always have digits before and after its decimal separator
#     • Number in a demon's name is considered everything that is a valid integer or floating point number (with dot '.' used as separator). For example, all these are valid numbers: '4', '+4', '-4', '3.5', '+3.5', '-3.5'
#
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
