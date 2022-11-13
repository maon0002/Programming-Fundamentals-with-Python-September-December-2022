input_string = input().replace(" ", "")
char_dictionary = {}
for char in input_string:
    if char not in char_dictionary.keys():
        char_dictionary[char] = 0
    char_dictionary[char] += 1

for char, occurrences in char_dictionary.items():
    print(f"{char} -> {occurrences}")
