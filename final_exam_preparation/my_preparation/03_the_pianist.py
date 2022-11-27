# Problem 3 - The Pianist
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#2.
#
# You are a pianist, and you like to keep a list of your favorite piano pieces. Create a program to help you organize it and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have. On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:
#     • "Add|{piece}|{composer}|{key}":
#         ◦ You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
#         ◦ If the piece is already in the collection, print:
# "{piece} is already in the collection!"
#     • "Remove|{piece}":
#         ◦ If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
#         ◦ Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
#     • "ChangeKey|{piece}|{new key}":
#         ◦ If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
#         ◦ Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"
# Input/Constraints
#     • You will receive a single integer at first – the initial number of pieces in the collection
#     • For each piece, you will receive a single line of text with information about it.
#     • Then you will receive multiple commands in the way described above until the command "Stop".
#     • All the output messages with the appropriate formats are described in the problem description.
# Output


def add_func(lst, collection_dict):
    add_piece = lst[1]
    add_composer = lst[2]
    add_key = lst[3]
    if add_piece not in collection_dict.keys():
        collection_dict[add_piece] = [add_composer, add_key]
        print(f"{add_piece} by {add_composer} in {add_key} added to the collection!")
    else:
        print(f"{add_piece} is already in the collection!")


def remove_func(lst, collection_dict):
    remove_piece = lst[1]
    if remove_piece in collection_dict.keys():
        del collection_dict[remove_piece]
        print(f"Successfully removed {remove_piece}!")
    else:
        print(f"Invalid operation! {remove_piece} does not exist in the collection.")


def changekey_func(lst, collection_dict):
    change_piece = lst[1]
    if change_piece in collection_dict.keys():
        change_key = lst[2]
        collection_dict[change_piece][1] = change_key
        print(f"Changed the key of {change_piece} to {change_key}!")
    else:
        print(f"Invalid operation! {change_piece} does not exist in the collection.")


def final_print_func(collection_dict):
    # collection_dict = dict(sorted(collection_dict.items())) #if we need to sort the 2nd part of the result
    for keys, values in collection_dict.items():
        print(f"{keys} -> Composer: {values[0]}, Key: {values[1]}")


def actions(collection_dict):

    while True:
        command_line = input()

        if command_line == "Stop":
            break
        command = command_line.split("|")
        action_name = command[0]

        if action_name == "Add":
            add_func(command, collection_dict)
        elif action_name == "Remove":
            remove_func(command, collection_dict)
        elif action_name == "ChangeKey":
            changekey_func(command, collection_dict)

    final_print_func(collection_dict)


def pieces_collection(num):
    collection_dict = {}
    while num:
        pieces_info = input().split("|")
        for item in pieces_info:
            piece = pieces_info[0]
            composer = pieces_info[1]
            key = pieces_info[2]
            collection_dict[piece] = [composer, key]
        num -= 1
    actions(collection_dict)


number_of_pieces_in_the_collection = int(input())
pieces_collection(number_of_pieces_in_the_collection)
