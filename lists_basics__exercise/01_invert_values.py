original_string = input()
splitted_list = original_string.split(" ")
inverted_list = []

for num in splitted_list:
    if "-" in num:
        num = num.replace("-", "")
        num = int(num)
        inverted_list.append(num)
    elif num == "0":
        num = int(num)
        inverted_list.append(num)
    else:
        num = "-" + num
        num = int(num)
        inverted_list.append(num)

print(inverted_list)
