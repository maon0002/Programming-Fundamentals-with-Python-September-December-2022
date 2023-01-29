def validate_pass(pass_str):
    pass_length = True
    pass_chars = True
    pass_2_digits = True
    if not 6 <= len(pass_str) <= 10:
        pass_length = False
        print(f"Password must be between 6 and 10 characters")

    digits_counter = 0
    for i in range(len(pass_str)):
        char = pass_str[i]
        if not char.isalnum():
            pass_chars = False
        if char.isdigit():
            digits_counter += 1
    if not pass_chars:
        print(f"Password must consist only of letters and digits")
    if digits_counter < 2:
        pass_2_digits = False
        print("Password must have at least 2 digits")

    if pass_length and pass_chars and pass_2_digits:
        print("Password is valid")


pass_input = input()
validate_pass(pass_input)
