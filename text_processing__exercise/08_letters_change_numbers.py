def letters_calc(command):
    total = 0
    for commands in command:
        first_letter = commands[0]
        last_letter = commands[-1]
        number = int(commands[1:-1])
        position = None
        if first_letter.isupper():
            position = ord(first_letter) - 64
            total += number / position
        elif first_letter.islower():
            position = ord(first_letter) - 96
            total += number * position
        if last_letter.isupper():
            position = ord(last_letter) - 64
            total -= position
        elif last_letter.islower():
            position = ord(last_letter) - 96
            total += position
    return f"{total:.2f}"


input_string = input().split()
input_list_without_spaces = [w.strip() for w in input_string]
print(letters_calc(input_list_without_spaces))
