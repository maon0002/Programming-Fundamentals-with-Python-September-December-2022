# Problem 1 - Secret Chat
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#0.
#
# You have plenty of free time, so you decide to write a program that conceals and reveals your received messages. Go ahead and type it in!
# On the first line of the input, you will receive the concealed message. After that, until the "Reveal" command is given, you will receive strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its actual content. There are several types of instructions, split by ":|:"
#     • "InsertSpace:|:{index}":
#         ◦ Inserts a single space at the given index. The given index will always be valid.
#     • "Reverse:|:{substring}":
#         ◦ If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
#         ◦ If not, print "error".
#         ◦ This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
#     • "ChangeAll:|:{substring}:|:{replacement}":
#         ◦ Changes all occurrences of the given substring with the replacement text.
# Input / Constraints
#     • On the first line, you will receive a string with a message.
#     • On the following lines, you will be receiving commands, split by ":|:".
# Output
#     • After each set of instructions, print the resulting string.
#     • After the "Reveal" command is received, print this message:
# "You have a new text message: {message}"
def change_all(substring, replacement, message_text):
    message_text = message_text.replace(substring, replacement)
    print(message_text)
    return message_text


def reverse(substring, message_text):
    if substring in message_text:
        message_text = message_text.replace(substring, "", 1)
        reversed_substring = substring[::-1]
        message_text = message_text + reversed_substring
        print(message_text)
        return message_text
    print("error")
    return message_text


def insert_space(index, message_text):
    message_text = (message_text[:index] + " " + message_text[index:])
    print(message_text)
    return message_text


def reveal(message_text):
    print(f"You have a new text message: {message_text}")


def main_func(message_text):
    while True:

        command = input()
        if command == "Reveal":
            reveal(message_text)
            break

        current_command = command.split(":|:")
        action = current_command[0]
        if action == "ChangeAll":
            substring = current_command[1]
            replacement = current_command[2]
            message_text = change_all(substring, replacement, message_text)
        elif action == "Reverse":
            substring = current_command[1]
            message_text = reverse(substring, message_text)
        elif action == "InsertSpace":
            index = int(current_command[1])
            message_text = insert_space(index, message_text)


concealed_message = input()
main_func(concealed_message)
