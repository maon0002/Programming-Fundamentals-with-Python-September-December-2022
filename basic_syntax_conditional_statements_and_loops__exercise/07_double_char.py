command = input()
string_for_print = ''
is_valid = True

while command != "End":

    for i in range(len(command)):

        if command == 'SoftUni':
            is_valid = False

        else:
            char = command[i]
            string_for_print += char * 2

    if is_valid:
        print(string_for_print)
        string_for_print = ''
        command = input()
    else:
        string_for_print = ''
        command = input()
        is_valid = True
