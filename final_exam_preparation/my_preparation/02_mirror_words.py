# Problem 2 - Mirror words
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#1.
#
# The SoftUni Spelling Bee competition is here. But it`s not like any other Spelling Bee competition out there. It`s different and a lot more fun! You, of course, are a participant, and you are eager to show the competition that you are the best, so go ahead, learn the rules and win!
# On the first line of the input, you will be given a text string. To win the competition, you have to find all hidden word pairs, read them, and mark the ones that are mirror images of each other.
# First of all, you have to extract the hidden word pairs. Hidden word pairs are:
#     • Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
#     • At least 3 characters long each (without the surrounding symbols)
#     • Made up of letters only
# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they are a match, and you have to store them somewhere. Examples of mirror words:
# #Part##traP# @leveL@@Level@ #sAw##wAs#
#     • If you don`t find any valid pairs, print: "No word pairs found!"
#     • If you find valid pairs print their count: "{valid pairs count} word pairs found!"
#     • If there are no mirror words, print: "No mirror words!"
#     • If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"
# Input / Constraints
#     • You will recive a string.
# Output
#     • Print the proper output messages in the proper cases as described in the problem description.
#     • If there are pairs of mirror words, print them in the end, each pair separated by ", ".
#     • Each pair of mirror word must be printed with " <=> " between the words.
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
    pattern = r'(@|#)([A-Za-z]{3,})\1(@|#)([A-Za-z]{3,})\1'
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
