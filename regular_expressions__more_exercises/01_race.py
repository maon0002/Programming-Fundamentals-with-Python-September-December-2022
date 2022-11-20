#     1. Race
# Write a program that processes information about a race. On the first line you will be given list of participants
# separated by ", ".
# On the next few lines until you receive a line "end of race" you will be given some info
# which will be some alphanumeric characters. In between them you could have some extra characters
# which you should ignore. For example: "G!32e%o7r#32g$235@!2e".
# The letters are the name of the person and the sum of the digits is the distance he ran.
# So here we have George who ran 29 km.
# Store the information about the person only if the list of racers contains the name of the person.
# If you receive the same person more than once just add the distance to his old distance.
# At the end print the top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"

import re

racers = input()
racers_dict = {names: 0 for names in list(racers.split(", "))}
command = input()

while command != "end of race":
    name_pattern = r'([A-Za-z]+)'
    distance_pattern = r'[0-9]+'
    name = "".join(re.findall(name_pattern, command))
    # name1 = re.compile(name_pattern)
    # name2 = name1.match(racers).group(0)
    distance = "".join(re.findall(distance_pattern, command))  # string of digits which must sum
    distance_calc = sum(int(digit) for digit in distance)
    if name in racers:
        racers_dict[name] += distance_calc

    command = input()

sorted_dict = sorted(racers_dict.items(), key=lambda x: x[1], reverse=True)
print(f"1st place: {sorted_dict[0][0]}")
print(f"2nd place: {sorted_dict[1][0]}")
print(f"3rd place: {sorted_dict[2][0]}")

