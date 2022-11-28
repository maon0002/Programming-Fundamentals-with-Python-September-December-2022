#     6. Sort
# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a sorted list of numbers in ascending order. Use sorted().


def sort_func(base_list):
    sorted_list = sorted(base_list)
    print(sorted_list)


input_line = list(map(int, input().split(" ")))
sort_func(input_line)
