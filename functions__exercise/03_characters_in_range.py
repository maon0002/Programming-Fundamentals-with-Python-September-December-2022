
def chars_range(first_char, second_char):
    for char in range(ord(first_char) + 1, ord(second_char)):
        print(chr(char), end=" ")


first_char = input()
second_char = input()

chars_range(first_char, second_char)
