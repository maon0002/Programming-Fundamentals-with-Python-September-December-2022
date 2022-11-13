def rounding(numbers):
    rounded_numbers = []
    for current_number in numbers:
        rounded_numbers.append(round(float(current_number)))
    return rounded_numbers


numbers_list_str = input().split()
print(rounding(numbers_list_str))