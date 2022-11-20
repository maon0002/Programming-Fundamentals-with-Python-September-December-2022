#     2. Match Phone Number
# Write a regular expression to match a valid phone number from Sofia. After you find all valid phones, print them on the console, separated by a comma and a space ", ".
# Compose the Regular Expression
# A valid number has the following characteristics:
#     • It starts with "+359"
#     • Then, it is followed by the area code (always 2)
#     • After that, it is followed by a number:
#         ◦ The number consists of 7 digits (separated into two groups of 3 and 4 digits, respectively).
#     • The different parts are separated by either a space or a hyphen ('-').

import re

pattern = r"(\+359)([ |-]{1})(2\2\d{3}\2\d{4})\b"
input_line = input()
output_line = re.findall(pattern, input_line)

result = []
for i in range(len(output_line)):
    result.append("".join(output_line[i]))

print(", ".join(result))
