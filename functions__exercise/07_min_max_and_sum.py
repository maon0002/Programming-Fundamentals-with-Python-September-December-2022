def define_nums(num_list):
    min_num = sorted(num_list)
    max_num = sorted(num_list, reverse=True)
    nums_sum = sum(num_list)
    print(f"The minimum number is {min_num[0]}")
    print(f"The maximum number is {max_num[0]}")
    print(f"The sum number is: {nums_sum}")


input_line = list(map(int, input().split(" ")))
define_nums(input_line)
