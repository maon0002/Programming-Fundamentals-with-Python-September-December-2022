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
