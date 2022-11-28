# Problem 1 - Password Reset
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2303#0.
#
# Yet again, you have forgotten your password. Naturally, it's not the first time this has happened. Actually, you got so tired of it that you decided to help yourself with an intelligent solution.
# Write a password reset program that performs a series of commands upon a predefined string. First, you will receive a string, and afterward, until the command "Done" is given, you will be receiving strings with commands split by a single space. The commands will be the following:
#     • "TakeOdd"
#         ◦  Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
#     • "Cut {index} {length}"
#         ◦ Gets the substring with the given length starting from the given index from the password and removes its first occurrence, then prints the password on the console.
#         ◦ The given index and the length will always be valid.
#     • "Substitute {substring} {substitute}"
#         ◦ If the raw password contains the given substring, replaces all of its occurrences with the substitute text given and prints the result.
#         ◦ If it doesn't, prints "Nothing to replace!".
# Input
#     • You will be receiving strings until the "Done" command is given.
# Output
#     • After the "Done" command is received, print:
#         ◦ "Your password is: {password}"
# Constraints
#     • The indexes from the "Cut {index} {length}" command will always be valid.

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
