import re

pattern = r"\b[A-Z]{1}[a-z]+[' ']{1}[A-Z]{1}[a-z]+\b"
input_string = input()
output_string = re.findall(pattern, input_string)
print(" ".join(output_string))
