def explode(char_seq):
    output_string = ""
    strength = 0
    for i in range(len(char_seq)):
        char = char_seq[i]
        if char == ">":
            current_strength = int(char_seq[i + 1])
            strength += current_strength
            output_string += char
        elif strength > 0 and char != ">":
            strength -= 1
        else:
            output_string += char
    return output_string


input_string = input()
print(explode(input_string))
