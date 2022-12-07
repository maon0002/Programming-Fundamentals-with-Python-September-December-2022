# def actions(word_def_dict, only_words):
#     # command = input()
#     command = "Test"
#     # command = "Hand Over"
#     if command == "Test":
#         for word_, definitions_ in word_def_dict.items():
#             if word_ in only_words:
#                 print(f"{word_}:")
#                 for current_definition in definitions_:
#                     print(f" -{current_definition}")
#     elif command == "Hand Over":
#         print(" ".join(word_def_dict.keys()))
#
#
# def words_definition_func(words_with_definitions, only_words):
#     words_with_definitions_list = list(map(str, words_with_definitions.split(" | ")))
#     word_def_dict = {}
#
#     for pairs in words_with_definitions_list:
#         word, definition = pairs.split(": ")
#         if word not in word_def_dict.keys():
#             word_def_dict[word] = []
#         word_def_dict[word].append(definition)
#     # print(word_def_dict)
#     actions(word_def_dict, only_words)
#     return word_def_dict
#
#
# words_with_definitions = 'care: worry, anxiety, or concern | care: a state of mind in which one is troubled | face: the front part of the head, from the forehead to the chin'
# only_words = 'care | kitchen | flower'
# words_definition_func(words_with_definitions, only_words)


def actions(word_def_dict, only_words):
    command = input()
    if command == "Test":
        for word_, definitions_ in word_def_dict.items():
            if word_ in only_words:
                print(f"{word_}:")
                for current_definition in definitions_:
                    print(f" -{current_definition}")
    elif command == "Hand Over":
        print(" ".join(word_def_dict.keys()))


def words_definition_func(words_with_definitions, only_words):
    words_with_definitions_list = list(map(str, words_with_definitions.split(" | ")))
    word_def_dict = {}

    for pairs in words_with_definitions_list:
        word, definition = pairs.split(": ")
        if word not in word_def_dict.keys():
            word_def_dict[word] = []
        word_def_dict[word].append(definition)
    # print(word_def_dict)
    actions(word_def_dict, only_words)
    return word_def_dict


words_with_definitions = input()
only_words = input()
words_definition_func(words_with_definitions, only_words)