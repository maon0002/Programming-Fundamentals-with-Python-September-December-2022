ban_list = input().split(", ")
text = input()
censored_text = text
for banned_word in ban_list:

    while banned_word in censored_text:
        replacement = "*" * len(banned_word)
        censored_text = censored_text.replace(banned_word, replacement)
print(censored_text)
