def perfect_num(num):
    temp_num = num
    divisors = int(num / 2 + 1)
    divisors_list = []
    # while temp_num > 0:
    for nums in range(divisors, 0, -1):
        if temp_num % nums == 0:
            divisors_list.append(nums)
            continue

    if sum(divisors_list) == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num_input = int(input())
perfect_num(num_input)
