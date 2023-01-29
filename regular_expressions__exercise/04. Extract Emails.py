import re

pattern = r'\s(([a-z0-9]+[\-\.\_a-z]*)[@]([a-z\-]+([\.][a-z]+)+))\b'
input_line = input()
output_line = re.findall(pattern, input_line)

for email in output_line:
    print(email[0])
