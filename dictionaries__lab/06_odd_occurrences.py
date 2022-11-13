string = input().lower()
input_string = string.split()
odd_dictionary = {}

for occurrence in input_string:
    if occurrence not in odd_dictionary.keys():
        odd_dictionary[occurrence] = 0
    odd_dictionary[occurrence] += 1

for key, value in odd_dictionary.items():
    if int(value) % 2 != 0:
        print(key, end=" ")
