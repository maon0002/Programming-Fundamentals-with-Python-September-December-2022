def is_contain(text, peace):
    is_present = []

    for word_substring in peace:
        for word in text:
            if word_substring in word:
                is_present.append(word_substring)
                break
    return is_present


substring_string = input().split(", ")
full_string = input().split(", ")
print(is_contain(full_string, substring_string))
