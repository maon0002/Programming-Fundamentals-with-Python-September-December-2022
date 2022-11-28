#     3. Characters in Range
# Write a function that receives two characters and returns a single string with all the characters in between them (according to the ASCII code), separated by a single space. Print the result on the console.


def chars_range(first_char, second_char):
    for char in range(ord(first_char) + 1, ord(second_char)):
        print(chr(char), end=" ")


first_char = input()
second_char = input()

chars_range(first_char, second_char)
