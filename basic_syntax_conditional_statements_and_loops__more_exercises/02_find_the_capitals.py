text = input()
list_of_upper = []

for i in range(len(text)):
    char = text[i]
    if char.isupper():
        list_of_upper.append(i)
    else:
        continue

print(list_of_upper)
