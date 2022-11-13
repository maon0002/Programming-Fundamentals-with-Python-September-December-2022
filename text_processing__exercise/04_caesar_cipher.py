def encrypted_msg(text):
    encrypted_message = ""
    for i in range(len(text)):
        encrypted_message += chr(ord(text[i]) + 3)
    return encrypted_message


input_message = input()
print(encrypted_msg(input_message))
