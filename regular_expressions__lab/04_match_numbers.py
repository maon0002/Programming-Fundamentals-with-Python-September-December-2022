import re
pattern = r'(^|(?<=\s))(-?)([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
input_line = input()
output_line = re.findall(pattern, input_line)
output_line2 = re.finditer(pattern, input_line)
result = []

for nums in output_line:
    result.append("".join(nums))
print(" ".join(result))
