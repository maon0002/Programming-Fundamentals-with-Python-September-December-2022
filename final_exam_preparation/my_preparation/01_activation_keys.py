# Problem 1 - Activation Keys
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#0.
#
# You are about to make some good money, but first, you need to think of a way to verify who paid for your product and who didn't. You have decided to let people use the software for a free trial period and then require an activation key to continue using the product. Before you can cash out, the last step is to design a program that creates unique activation keys for each user. So, waste no more time and start typing!
# The first line of the input will be your raw activation key. It will consist of letters and numbers only.
# After that, until the "Generate" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the raw activation key.
# There are several types of instructions, split by ">>>":
#     • "Contains>>>{substring}":
#         ◦ If the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
#         ◦ Otherwise, prints: "Substring not found!"
#     • "Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
#         ◦ Changes the substring between the given indices (the end index is exclusive) to upper or lower case and then prints the activation key.
#         ◦ All given indexes will be valid.
#     • "Slice>>>{startIndex}>>>{endIndex}":
#         ◦ Deletes the characters between the start and end indices (the end index is exclusive) and prints the activation key.
#         ◦ Both indices will be valid.
# Input
#     • The first line of the input will be a string consisting of letters and numbers only.
#     • After the first line, until the "Generate" command is given, you will be receiving strings.
# Output
#     • After the "Generate" command is received, print:
#         ◦ "Your activation key is: {activation key}"

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
