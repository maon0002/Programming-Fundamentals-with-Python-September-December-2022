# Problem 1 - The Imitation Game
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#0.
#
# During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma code. Your job is to create a program to crack the codes.
# On the first line of the input, you will receive the encrypted message. After that, until the "Decode" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its true content. There are several types of instructions, split by '|'
#     • "Move {number of letters}":
#         ◦ Moves the first n letters to the back of the string
#     • "Insert {index} {value}":
#         ◦ Inserts the given value before the given index in the string
#     • "ChangeAll {substring} {replacement}":
#         ◦ Changes all occurrences of the given substring with the replacement text
# Input / Constraints
#     • On the first line, you will receive a string with a message.
#     • On the following lines, you will be receiving commands, split by '|' .
# Output
#     • After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"

#
# def move(letters_qty):
#     text = initial_command
#     start_position = len(text) - letters_qty
#     decoded_message(text[start_position:] + text[0:start_position])
#
#
# # • "Move {number of letters}":
# #     ◦ Moves the first n letters to the back of the string
# def insert(i, val):
#     text = initial_command
#     # index_before = i - 1
#     inserted_text = text[0:i] + val + text[i:]
#     decoded_message(inserted_text)
#
#
# def change_all(substr, replace):
#     text = initial_command
#     change = text.replace(substr, replace)
#     decoded_message(change)
#
#
# def message_values(text):
#     encrypted_message = text.split("|")
#     current_command = encrypted_message[0]
#     if current_command == "Insert":
#         index = encrypted_message[1]
#         value = encrypted_message[2]
#         insert(int(index), value)
#     elif current_command == "ChangeAll":
#         substring = encrypted_message[1]
#         replacement = encrypted_message[2]
#         change_all(substring, replacement)
#     elif current_command == "Move":
#         number_of_letters = encrypted_message[1]
#         move(int(number_of_letters))
#
#
# def decoded_message(text):
#     temp_text = text
#     final_message = temp_text
#     print(final_message)
#
#
# initial_command = input()
# final_message = ""
#
# while True:
#     command = input()
#
#     if command == "Decode":
#         break
#
#     message_values(command)


def move(text, letters_qty):
    return text[letters_qty:] + text[0:letters_qty]


def insert(text, i, val):
    inserted_text = text[0:i] + val + text[i:]
    return inserted_text


def change_all(text, substr, replace):
    change = text.replace(substr, replace)
    return change


initial_command = input()
final_message = initial_command

while True:
    command = input()

    if command == "Decode":
        break

    encrypted_message = command.split("|")
    current_command = encrypted_message[0]
    if current_command == "Insert":
        index = encrypted_message[1]
        value = encrypted_message[2]
        final_message = insert(final_message, int(index), value)

    elif current_command == "ChangeAll":
        substring = encrypted_message[1]
        replacement = encrypted_message[2]
        final_message = change_all(final_message, substring, replacement)

    elif current_command == "Move":
        number_of_letters = encrypted_message[1]
        final_message = move(final_message, int(number_of_letters))

print(f"The decrypted message is: {final_message}")
