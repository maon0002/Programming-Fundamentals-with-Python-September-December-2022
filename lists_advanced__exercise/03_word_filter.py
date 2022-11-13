def even_strings(words):
    filtered_by_even = [word for word in words if len(word) % 2 == 0]
    result = "\n".join(filtered_by_even)
    return result


text = input().split()
print(even_strings(text))
