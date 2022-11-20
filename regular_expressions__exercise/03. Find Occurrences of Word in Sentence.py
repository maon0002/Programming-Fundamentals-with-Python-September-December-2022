#     3. Find Occurrences of Word in Sentence
# Write a program that finds how many times a word is used in a string.
# The output is a single number indicating the number of times the string contains the word.
# Note that letter case does not matter – it is case-insensitive.


import re

input_line = input()
occurred_word = input()
pattern = fr'\b{occurred_word}\b'
output_line = re.findall(pattern, input_line, flags=re.IGNORECASE)
result = []
for occurrences in output_line:
    result.append(occurrences)
print(len(result))
