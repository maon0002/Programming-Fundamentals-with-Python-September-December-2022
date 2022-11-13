def positive_nums(lst):
    positive_list = [n for n in lst if int(n) >= 0]
    return ", ".join(positive_list)


def negative_nums(lst):
    negative_list = [n for n in lst if int(n) < 0]
    return ", ".join(negative_list)


def even_nums(lst):
    even_list = [n for n in lst if int(n) % 2 == 0]
    return ", ".join(even_list)


def odd_nums(lst):
    odd_list = [n for n in lst if int(n) % 2 != 0]
    return ", ".join(odd_list)


input_string = input().split(", ")

print(f"Positive: {positive_nums(input_string)}")
print(f"Negative: {negative_nums(input_string)}")
print(f"Even: {even_nums(input_string)}")
print(f"Odd: {odd_nums(input_string)}")
