
def take_odd(init_string):
    new_string = ""
    for i in range(len(init_string)):
        char = init_string[i]
        if i % 2 != 0:
            new_string += char
    print(new_string)
    return new_string


def cut(init_string, index, length):
    init_string = init_string.replace(init_string[index:index + length], "", 1)
    print(init_string)
    return init_string


def substitute(init_string, substring, substitute):
    if substring in init_string:
        init_string = init_string.replace(substring, substitute)
        print(init_string)
        return init_string
    print("Nothing to replace!")
    return init_string


def print_result(init_string):
    print(f"Your password is: {init_string}")
    return init_string


def pass_reset(init_string):
    while True:
        command = input()
        if command == "Done":
            print_result(init_string)
            break

        if command == "TakeOdd":
            init_string = take_odd(init_string)

        temp_command = command.split(" ")
        current_command = temp_command[0]

        if current_command == "Cut":
            first_value = temp_command[1]
            second_value = temp_command[2]
            init_string = cut(init_string, int(first_value), int(second_value))
        elif current_command == "Substitute":
            first_value = temp_command[1]
            second_value = temp_command[2]
            init_string = substitute(init_string, first_value, second_value)


predefined_string = input()
pass_reset(predefined_string)
