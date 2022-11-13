def is_palindrome(word):
    if word == word[::-1]:
        return word


def palindrome_count(lst):
    counter = lst.count(palindrome)
    return counter


text = input().split()
palindrome = input()
palindrome_list = [word for word in text if is_palindrome(word)]

print(palindrome_list)
print(f"Found palindrome {palindrome_count(palindrome_list)} times")
