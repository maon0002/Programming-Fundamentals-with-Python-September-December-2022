def smallest_numbers():
    numbers_list = []
    for nums in range(3):
        current_number = int(input())
        numbers_list.append(current_number)

    numbers_list.sort()
    print(numbers_list[0])
    return numbers_list[0]


smallest_numbers()
