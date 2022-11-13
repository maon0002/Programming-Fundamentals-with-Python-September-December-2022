number_of_lines = int(input())
total_sum = 0

for i in range(number_of_lines):
    current_char = input()
    char_value = ord(current_char)
    total_sum += char_value

print(f"The sum equals: {total_sum}")
