# Problem 2 - Ad Astra
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#1.
#
# You are an astronaut who just embarked on a mission across the solar system. Since you will be in space for a long time, you have packed a lot of food with you. Create a program, which helps you identify how much food you have left and gives you information about its expiration date.
# On the first line of the input, you will be given a text string. You must extract the information about the food and calculate the total calories.
# First, you must extract the food info. It will always follow the same pattern rules:
#     • It will be surrounded by "|" or "#" (only one of the two) in the following pattern:
# #{item name}#{expiration date}#{calories}#   or
# |{item name}|{expiration date}|{calories}|
#     • The item name will contain only lowercase and uppercase letters and whitespace
#     • The expiration date will always follow the pattern: "{day}/{month}/{year}", where the day, month, and year will be exactly two digits long
#     • The calories will be an integer between 0-10000
# Calculate the total calories of all food items and then determine how many days you can last with the food you have. Keep in mind that you need 2000kcal a day.
# Input / Constraints
#     • You will receive a single string
# Output
#     • First, print the number of days you will be able to last with the food you have:
# "You have food to last you for: {days} days!"
#     • The output for each food item should look like this:
# "Item: {item name}, Best before: {expiration date}, Nutrition: {calories}"

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
