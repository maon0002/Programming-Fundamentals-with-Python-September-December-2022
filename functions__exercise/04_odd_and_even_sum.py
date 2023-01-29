def odd_sum(num_string):
    odd_list = []
    for i in range(len(num_string)):
        current_num = int(num_string[i])
        if current_num % 2 != 0:
            odd_list.append(current_num)
    odd_result = f"Odd sum = {sum(odd_list)}"
    result.append(odd_result)
    return odd_result


def even_sum(num_string):
    even_list = []
    for i in range(len(num_string)):
        current_num = int(num_string[i])
        if current_num % 2 == 0:
            even_list.append(current_num)
    even_result = f"Even sum = {sum(even_list)}"
    result.append(even_result)
    return even_result


def print_result(final_list):
    print(", ".join(final_list))


single_number = input()
result = []
odd_sum(single_number)
even_sum(single_number)
print_result(result)
