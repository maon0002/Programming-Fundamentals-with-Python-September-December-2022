
def print_func(raw_activation_key):
    print(f"Your activation key is: {raw_activation_key}")
    # print( raw_activation_key == "abgHIjkLMNOPQRstuvwxyz")
    return f"Your activation key is: {raw_activation_key}"


def contains(substring_contains, raw_activation_key):
    if substring_contains in raw_activation_key:
        print(f"{raw_activation_key} contains {substring_contains}")
        return raw_activation_key
    print(f"Substring not found!")
    return raw_activation_key


def flip(upper_or_lower, start_index, end_index, raw_activation_key):
    string_for_replacement = raw_activation_key[start_index: end_index]
    raw_activation_key = raw_activation_key.replace(string_for_replacement, "`````")
    if upper_or_lower == "Upper":
        string_for_replacement = string_for_replacement.upper()
        raw_activation_key = raw_activation_key.replace("`````", string_for_replacement)
        print(raw_activation_key)
        return raw_activation_key
    elif upper_or_lower == "Lower":
        string_for_replacement = string_for_replacement.lower()
        raw_activation_key = raw_activation_key.replace("`````", string_for_replacement)
        print(raw_activation_key)
        return raw_activation_key


def slice_func(start_index_slice, end_index_slice, raw_activation_key):
    string_for_slicing = raw_activation_key[start_index_slice:end_index_slice]
    raw_activation_key = raw_activation_key.replace(string_for_slicing, "")
    print(raw_activation_key)
    return raw_activation_key


def activation_func(raw_activation_key):
    while True:
        command_line = input()
        if command_line == "Generate":
            print_func(raw_activation_key)
            break

        command = command_line.split(">>>")
        action = command[0]
        if action == "Contains":
            substring_contains = command[1]
            raw_activation_key = contains(substring_contains, raw_activation_key)
        elif action == "Flip":
            upper_or_lower = command[1]
            start_index = int(command[2])
            end_index = int(command[3])
            raw_activation_key = flip(upper_or_lower, start_index, end_index, raw_activation_key)
        elif action == "Slice":
            start_index_slice = int(command[1])
            end_index_slice = int(command[2])
            raw_activation_key = slice_func(start_index_slice, end_index_slice, raw_activation_key)


raw_activation_key = input()
activation_func(raw_activation_key)
