#     7. Min Max and Sum
# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
# The output should be as follows:
#     • On the first line: "The minimum number is {minimum number}"
#     • On the second line: "The maximum number is {maximum number}"
#     • On the third line: "The sum number is: {sum of all numbers}"


def define_nums(num_list):
    min_num = sorted(num_list)
    max_num = sorted(num_list, reverse=True)
    nums_sum = sum(num_list)
    print(f"The minimum number is {min_num[0]}")
    print(f"The maximum number is {max_num[0]}")
    print(f"The sum number is: {nums_sum}")


input_line = list(map(int, input().split(" ")))
define_nums(input_line)
