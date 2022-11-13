def message(seq, text):
    message_str = []
    for current_index in seq:
        digits_sum = 0
        index_overwrite = 0
        for current_digit in current_index:
            digits_sum += int(current_digit)

        if digits_sum > len(text):
            index_overwrite = digits_sum - len(text)
            message_str.append(text[index_overwrite])
            text = (text[0:index_overwrite:]) + (text[index_overwrite + 1::])
        else:
            message_str.append(text[digits_sum])
            text = text[0: digits_sum:] + text[digits_sum + 1::]
    return "".join(message_str)


number_sequence_input = input().split()
string_input = input()
print(message(number_sequence_input, string_input))
