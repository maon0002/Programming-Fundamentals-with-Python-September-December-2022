def change_func(char, replacement, init_string):
    init_string = init_string.replace(char, replacement)
    print(init_string)
    return init_string


def includes_func(incl_substring, init_string):
    if incl_substring in init_string:
        return True
    return False


def end_func(end_substring, init_string):
    if init_string.endswith(end_substring):
        return True
    return False


def uppercase_func(init_string):
    init_string = init_string.upper()
    return init_string


def find_index_func(char_index, init_string):
    index_position = init_string.index(char_index)
    return index_position


def cut_func(start_index, count, init_string):
    end_index = start_index + count
    cut_string = init_string[start_index:end_index]
    return cut_string


def string_game(init_string):
    while True:
        command = input()
        if command == "Done":
            break

        current_command = command.split()
        action = current_command[0]
        if action == "Change":
            char = current_command[1]
            replacement = current_command[2]
            init_string = change_func(char, replacement, init_string)
        elif action == "Includes":
            incl_substring = current_command[1]
            print(includes_func(incl_substring, init_string))
        elif action == "End":
            end_substring = current_command[1]
            print(end_func(end_substring, init_string))
        elif action == "Uppercase":
            init_string = uppercase_func(init_string)
            print(uppercase_func(init_string))
        elif action == "FindIndex":
            char_index = current_command[1]
            print(find_index_func(char_index, init_string))
        elif action == "Cut":
            start_index = int(current_command[1])
            count = int(current_command[2])
            print(cut_func(start_index, count, init_string))


input_line = input()
string_game(input_line)
