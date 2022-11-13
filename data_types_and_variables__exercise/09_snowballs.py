number_of_snowballs = int(input())
snowball_weight = ""
snowball_time = ""
snowball_quality = ""
# value = int((snowball_weight / snowball_time) ** snowball_quality)
prev_value = 0
prev_max_result = ""

for x in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = int((snowball_weight / snowball_time) ** snowball_quality)

    if value > prev_value:
        prev_value = value
        prev_max_result = f"{snowball_weight} : {snowball_time} = {value} ({snowball_quality})"

print(prev_max_result)
