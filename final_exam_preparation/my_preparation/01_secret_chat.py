
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
