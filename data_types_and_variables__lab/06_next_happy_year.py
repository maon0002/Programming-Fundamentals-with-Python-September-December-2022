year = int(input())
# year = 9999

is_happy_year = False
unique_digits = ""

while not is_happy_year:
    year += 1
    str_year = str(year)
    for digit in range(len(str_year)):
        if str_year[digit] not in unique_digits:
            unique_digits += str_year[digit]

    if len(unique_digits) == len(str_year):
        is_happy_year = True
        break
    else:
        unique_digits = ""

print(unique_digits)
