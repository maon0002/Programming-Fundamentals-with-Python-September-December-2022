def zeroes_to_back(numbers):
    non_zeroes = []
    zeroes = []
    for digit in numbers:
        if digit == "0":
            zeroes.append(int(digit))
        else:
            non_zeroes.append(int(digit))
    merged_digits = non_zeroes + zeroes
    return merged_digits


numbers_str_input = input().split(", ")
print(zeroes_to_back(numbers_str_input))
