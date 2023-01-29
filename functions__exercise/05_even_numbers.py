
# def split_even(nums):
#     even_nums = []
#     for num in nums:
#         if int(num) % 2 == 0:
#             even_nums.append(int(num))
#     print(even_nums)
#
#
# input_line = input().split()
# split_even(input_line)


# def split_even(nums):
#     int_list = [int(x) for x in nums]
#     result = list(filter(lambda x: (x % 2 == 0), int_list))
#     print(result)
#
#
# input_line = input().split(" ")
# split_even(input_line)


def split_even(nums):
    result = list(filter(lambda x: (x % 2 == 0), nums))
    print(result)

#OPTION1
# input_line = input().split(" ")
# input_line = list(map(int, input_line))

#OPTION2
input_line = list(map(int, input().split(" ")))
split_even(input_line)


