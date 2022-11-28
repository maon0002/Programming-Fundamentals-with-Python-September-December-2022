#     8. Palindrome Integers
# A palindrome is a number that reads the same backward as forward, such as 323 or 1001. Write a function that receives a list of positive integers, separated by comma and space ", ". The function should check if each integer is a palindrome - True or False. Print the result.


def palindrome(nums_list):
    for nums in nums_list:
        if nums == nums[::-1]:
            print("True")
        else:
            print("False")


input_line = input().split(", ")
palindrome(input_line)
