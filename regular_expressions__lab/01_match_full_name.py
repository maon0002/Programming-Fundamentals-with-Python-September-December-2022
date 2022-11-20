#     1. Match Full Name
# Write a program to match full names from a sequence of characters and print them on the console.
# Writing the Regular Expression
# First, write a regular expression to match a valid full name, according to these conditions:
#     • A valid full name has the following characteristics:
#         ◦ It consists of two words.
#         ◦ Each word starts with a capital letter.
#         ◦ After the first letter, it only contains lowercase letters.
#         ◦ Each of the two words should be at least two letters long.
#         ◦ A single space separates the two words.

import re

pattern = r"\b[A-Z]{1}[a-z]+[' ']{1}[A-Z]{1}[a-z]+\b"
input_string = input()
output_string = re.findall(pattern, input_string)
print(" ".join(output_string))
