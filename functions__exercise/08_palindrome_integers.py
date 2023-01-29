def palindrome(nums_list):
    for nums in nums_list:
        if nums == nums[::-1]:
            print("True")
        else:
            print("False")


input_line = input().split(", ")
palindrome(input_line)
