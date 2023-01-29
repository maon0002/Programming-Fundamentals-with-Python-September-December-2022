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

