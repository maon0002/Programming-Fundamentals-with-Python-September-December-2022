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
