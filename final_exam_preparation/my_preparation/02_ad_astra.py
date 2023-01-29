
# import re
#
# input_line = input()
# pattern = r'([#|\|])([A-Za-z\s]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1([\d]+)\1'
#
# matched_groups = re.findall(pattern, input_line)
# info_extract = []
# total_calories = 0
#
# for group in matched_groups:
#     item_name, expiration_date, calories = group[1], group[2], group[3]
#     info_extract.append(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
#     total_calories += int(calories)
#
# print(f"You have food to last you for: {int(total_calories / 2000)} days!")
# print("\n".join(info_extract))

#----------------w/o func
# import re
#
# input_line = input()
# pattern = r'([#|\|])([A-Za-z\s]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1([\d]+)\1'
#
# matched_groups = re.findall(pattern, input_line)
# info_extract = []
# total_calories = 0
#
# for group in matched_groups:
#     item_name, expiration_date, calories = group[1], group[2], group[3]
#     info_extract.append(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
#     total_calories += int(calories)
#
# print(f"You have food to last you for: {int(total_calories / 2000)} days!")
# print("\n".join(info_extract))

import re


def calculate(calories):
    days_left = int(calories / 2000)
    return days_left


def extract_info(text):
    info_extract = []
    calories_lst = []
    pattern = r'([#|\|])([A-Za-z\s]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1([\d]+)\1'
    matched_groups = re.findall(pattern, text)

    for group in matched_groups:
        item_name, expiration_date, calories = group[1], group[2], group[3]
        info_extract.append(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {int(calories)}")
        calories_lst.append(int(calories))
    calculate(sum(calories_lst))
    print_result(info_extract, (calculate(sum(calories_lst))))
    return info_extract


def print_result(info, days):
    print(f"You have food to last you for: {days} days!")
    print("\n".join(info))


input_text = input()
extract_info(input_text)
