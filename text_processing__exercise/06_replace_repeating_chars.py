def repeating_chars_replacement(text):
    output_string = " "
    previous_char = " "
    for i in range(len(text)):
        char = text[i]
        if output_string[-1] != char:
            output_string += char
    return output_string[1::]


input_string = input()
print(repeating_chars_replacement(input_string))
