text = input().split(", ")
sorted_list = sorted(text, key=lambda x: (-len(x), x))

print(sorted_list)
