number_of_lines = int(input())
key_word = input()
string_list = []
matching_word_list = []

for checks in range(number_of_lines):
    current_string = input()
    string_list.append(current_string)
    if key_word in current_string:
        matching_word_list.append(current_string)

print(string_list)
print(matching_word_list)
