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

    # print(found_matches, count_matches, emoji_treshold, cool_treshold) #test
    print_result(count_matches, emoji_treshold, cool_treshold)
    return found_matches, count_matches, emoji_treshold, cool_treshold


def print_result(count_matches, emoji_treshold, cool_treshold):
    print(f"Cool threshold: {cool_treshold}")
    print(f"{count_matches} emojis found in the text. The cool ones are:")
    for current_emojies, treshold in emoji_treshold.items():
        if treshold > cool_treshold:
            print(current_emojies)
    return emoji_treshold.items()


input_string = input()
emoji_validation(input_string)
