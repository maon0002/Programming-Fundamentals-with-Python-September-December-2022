#
#     1. Capture the Numbers
# Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space.


import re

pattern = r'\d+'
input_line = input()
result = []
while input_line:
    matches = re.findall(pattern, input_line)
    if matches:
        result.append(" ".join(matches))
    input_line = input()

print(" ".join(result))
