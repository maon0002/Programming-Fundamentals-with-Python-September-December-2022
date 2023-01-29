import re


def print_result(mirror_list, words_list):
    if not words_list:
        print("No word pairs found!")
    if words_list:
        print(f"{len(words_list) / 2:.0f} word pairs found!")
    if not mirror_list:
        print(f"No mirror words!")
    if mirror_list:
        print("The mirror words are:")
        print(", ".join(mirror_list))


def mirror_words(words_list):
    list_of_mirror_words = []
    for i in range(0, len(words_list), 2):
        word = words_list[i]
        mirror_word = word[::-1]
        for i in range(1, len(words_list), 2):
            current_word = words_list[i]
            if current_word == mirror_word:
                string_to_add = f"{word} <=> {mirror_word}"
                if string_to_add[::-1] not in list_of_mirror_words:
                    list_of_mirror_words.append(f"{word} <=> {mirror_word}")

    print_result(list_of_mirror_words, words_list)
    # print(list_of_mirror_words)
    return list_of_mirror_words


def find_words(text):
    pattern = r'(@|#)([A-Za-z]{3,})\1(@|#)([A-Za-z]{3,})\1' #(\1{2})
    matches = re.findall(pattern, text)
    matches_list = []
    for group in matches:
        for indexes in range(len(group)):
            if indexes in [1, 3]:
                add_word = group[indexes]
                matches_list.append(add_word)
    # print(matches_list)
    mirror_words(matches_list)
    return matches_list


input_line = input()
find_words(input_line)
