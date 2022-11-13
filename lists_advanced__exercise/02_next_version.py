def version_number(string):
    digit_string = string.replace(".", "")
    ver = ""
    digits = int(digit_string) + 1
    digits = str(digits)
    for i in range(len(digit_string)):
        if i < len(digit_string) - 1:
            ver += digits[i] + "."
        else:
            ver += digits[i]
    return ver


version_string = input()
print(version_number(version_string))
