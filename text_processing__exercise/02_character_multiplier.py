input_string = input()
first_string, second_string = input_string.split()
total_sum = 0

if len(first_string) == len(second_string):
    for i in range(len(first_string)):
        total_sum += ord(first_string[i]) * ord(second_string[i])

elif len(first_string) > len(second_string):
    for i in range(len(second_string)):
        total_sum += ord(first_string[i]) * ord(second_string[i])
    for i in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[i])

elif len(second_string) > len(first_string):
    for i in range(len(first_string)):
        total_sum += ord(first_string[i]) * ord(second_string[i])
    for i in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[i])

print(total_sum)
