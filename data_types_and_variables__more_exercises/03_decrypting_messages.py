key = int(input())
number_of_inputs = int(input())
end_string = ''

for x in range(1, number_of_inputs + 1):
    current_char = input()
    lower_char = current_char.lower()
    ascii_new_position = ord(current_char) + key
    decrypted_char = chr(ascii_new_position)
    if current_char.islower():
        end_string += decrypted_char.lower()
    else:
        end_string += decrypted_char.upper()

print(end_string)
