# Problem 2 - Emoji Detector
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#1.
#
# Your task is to write a program that extracts emojis from a text and find the threshold based on the input.
# You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.  The cool threshold could be a huge number, so be mindful.
# An emoji is valid when:
#     • It is surrounded by 2 characters, either "::" or "**"
#     • It is at least 3 characters long (without the surrounding symbols)
#     • It starts with a capital letter
#     • Continues with lowercase letters only
# Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
# Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
# You need to count all valid emojis in the text and calculate their coolness. The coolness of the emoji is determined by summing all the ASCII values of all letters in the emoji.
# Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
# You need to print the result of the cool threshold and, after that to take all emojis out of the text, count them and print only the cool ones on the console.
# Input
#     • On the single input, you will receive a piece of string.
# Output
#     • On the first line of the output, print the obtained Cool threshold in the format:
# "Cool threshold: {coolThresholdSum}"
#     • On the following line, print the count of all emojis found in the text in format:
# "{countOfAllEmojis} emojis found in the text. The cool ones are:
# {cool emoji 1}
# {cool emoji 2}
# …
# {cool emoji N}"
# Constraints
# There will always be at least one digit in the text!
# import re
#
#
# def cool_calculation(input_string):
#     cool_pattern = r'(\d)'  # r'([:|*]{2})([A-Z]{1}[a-z]{2,})\1'
#     digit_matches = re.findall(cool_pattern, input_string)
#     temp_cool_treshold = 1
#     # digits print  ['3', '1', '1', '3', '1', '1', '2', '3', '5', '2', '1']
#     for digit in digit_matches:
#         current_digit = int(digit)
#         temp_cool_treshold *= current_digit
#     return temp_cool_treshold
#
#
# def emoji_validation(input_string):
#     pattern = r'([:|*]{2})([A-Z]{1}[a-z]{2,})\1|(\d)'  # r'([:|*]{2})([A-Z]{1}[a-z]{2,})\1'
#     matches = re.findall(pattern, input_string)
#     # [('::', 'Smiley'), ('**', 'Tigers'), ('::', 'Mooning'), ('**', 'Shy')]
#     print("first print ", matches)
#     found_matches = [emoji[1] for emoji in matches if emoji[1]]
#     count_matches = len(found_matches)
#     # cool_treshold_list = [emoji[2] for emoji in matches if int(emoji[2]) > -1]
#     # print(cool_treshold_list)
#
#     cool_treshold = cool_calculation(input_string)
#     print("cool treshold is: ", cool_treshold)
#
#     emoji_treshold = {}
#     for emojies in found_matches:
#         # emoji_treshold.append(emojies)
#         emoji_treshold[emojies] = 0
#         for i in range(len(emojies)):
#             value = ord(emojies[i])
#             emoji_treshold[emojies] += value
#     print("emoji tresholds are: ", emoji_treshold)
#
#     print(found_matches, count_matches, emoji_treshold, cool_treshold)
#     print_result(found_matches, count_matches, emoji_treshold, cool_treshold)
#     return found_matches, count_matches, emoji_treshold, cool_treshold
#
#
# def print_result(found_matches, count_matches, emoji_treshold, cool_treshold):
#     print(f"Cool threshold: {cool_treshold}")
#     print(f"{count_matches} emojis found in the text. The cool ones are:")
#     for current_emojies, treshold in emoji_treshold.items():
#         if treshold >= cool_treshold:
#             print(current_emojies)
#
#
# input_string = input()
# emoji_validation(input_string)


import re


def cool_calculation(input_string):
    cool_pattern = r'(\d)'  # r'([:|*]{2})([A-Z]{1}[a-z]{2,})\1'
    digit_matches = re.findall(cool_pattern, input_string)
    temp_cool_treshold = 1
    for digit in digit_matches:
        current_digit = int(digit)
        temp_cool_treshold *= current_digit
    return temp_cool_treshold


def emoji_validation(input_string):
    pattern = r'([*]{2}[A-Z]{1}[a-z]{2,}[*]{2})|([:]{2}[A-Z]{1}[a-z]{2,}[:]{2})'  # r'([:|*]{2})([A-Z]{1}[a-z]{2,})\1'
    matches = re.findall(pattern, input_string)
    found_matches = []
    for valid_emoji in matches:
        for valid_value in valid_emoji:
            if valid_value:
                found_matches.append(valid_value)

    count_matches = len(found_matches)

    cool_treshold = cool_calculation(input_string)

    emoji_treshold = {}
    for emojies in found_matches:
        emoji_treshold[emojies] = 0
        for i in range(len(emojies)):
            value = ord(emojies[i])
            emoji_treshold[emojies] += value

    # print(found_matches, count_matches, emoji_treshold, cool_treshold)
    print_result(count_matches, emoji_treshold, cool_treshold)
    return found_matches, count_matches, emoji_treshold, cool_treshold


def print_result(count_matches, emoji_treshold, cool_treshold):
    print(f"Cool threshold: {cool_treshold}")
    print(f"{count_matches} emojis found in the text. The cool ones are:")
    for current_emojies, treshold in emoji_treshold.items():
        if treshold > cool_treshold:
            print(current_emojies)
    return None


input_string = input()
emoji_validation(input_string)
