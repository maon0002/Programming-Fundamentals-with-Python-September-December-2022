def command_separator(text):
    rage_msg = ""
    current_text = ""
    repetition = 0
    for i in range(len(text)):
        char = text[i]
        if char.isdigit():
            repetition += int(char)
            if repetition == 0:
                rage_msg += current_text
            else:
                rage_msg += current_text * repetition
            current_text = ""
            repetition = 0
        else:
            current_text += char.upper()

    unique_symbols = len(set(rage_msg))
    return f"Unique symbols used: {unique_symbols}\n" \
           f"{rage_msg}"


input_string = input()

print(command_separator(input_string))
