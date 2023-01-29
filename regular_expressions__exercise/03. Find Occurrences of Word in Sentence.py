import re

input_line = input()
occurred_word = input()
pattern = fr'\b{occurred_word}\b'
output_line = re.findall(pattern, input_line, flags=re.IGNORECASE)
result = []
for occurrences in output_line:
    result.append(occurrences)
print(len(result))
