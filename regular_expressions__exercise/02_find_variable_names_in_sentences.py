import re

pattern = r'\b_([A-Za-z0-9]+)\b'
input_line = input()
output_line = re.findall(pattern, input_line)
print(",".join(output_line))
