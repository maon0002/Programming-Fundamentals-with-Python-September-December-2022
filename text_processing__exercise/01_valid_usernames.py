def username_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def username_syntax(username):
    for char in username:
        if not (char.isalnum() or char == "_" or char == "-"):
            return False
    return True


def username_spaces(username):
    for char in username:
        if not char == " ":
            return True
        return False


def username_validation(username):
    if username_length(username) and username_syntax(username) and username_spaces(username):
        return True
    return False


input_string = input().split(", ")

for usernames in input_string:
    if username_validation(usernames):
        print(usernames)
