number_of_lines = int(input())
all_current_numbers_list = []

COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'

for nums in range(number_of_lines):
    current_num = int(input())
    all_current_numbers_list.append(current_num)

command = input()
filtered_list = []

for number in all_current_numbers_list:

    filtered_numbers = (
            (command == COMMAND_EVEN and number % 2 == 0) or
            (command == COMMAND_ODD and number % 2 != 0) or
            (command == COMMAND_NEGATIVE and number < 0) or
            (command == COMMAND_POSITIVE and number >= 0)
    )
    if filtered_numbers:
        filtered_list.append(number)

print(filtered_list)
