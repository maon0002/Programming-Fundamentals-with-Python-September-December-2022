input_string = input()
digits = ""
letters = ""
symbols = ""

for chars in range(len(input_string)):
    char = input_string[chars]
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        symbols += char

print(digits)
print(letters)
print(symbols)
