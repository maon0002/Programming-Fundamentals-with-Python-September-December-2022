def group_of_tens(nums):
    max_number = max(nums)
    index_group = max_number // 10

    counter_min = 0

    for group in range(1, index_group + 2):
        group_min = counter_min * 10  # 0, 10, 20, 30 ... with latency
        group_max = group * 10  # 10, 20, 30 ...
        temp_lst = []
        for current_number in nums:

            if current_number in range(group_min + 1, group_max + 1):
                temp_lst.append(current_number)

        if not bool(temp_lst) and group == index_group + 1:
            break
        print(f"Group of {group}0's: {temp_lst}")
        counter_min += 1


numbers_string = input().split(", ")
numbers_digit = [int(number) for number in numbers_string]
group_of_tens(numbers_digit)
