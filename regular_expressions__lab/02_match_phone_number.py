import re

pattern = r"(\+359)([ |-]{1})(2\2\d{3}\2\d{4})\b"
input_line = input()
output_line = re.findall(pattern, input_line)

result = []
for i in range(len(output_line)):
    result.append("".join(output_line[i]))

print(", ".join(result))
