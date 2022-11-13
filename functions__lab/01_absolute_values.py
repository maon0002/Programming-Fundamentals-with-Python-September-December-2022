def abs_values(num_list):
    float_list = []
    for current_number in num_list:
        float_list.append(abs(float(current_number)))
    return f"{float_list}"


num_string = input().split(" ")
print(abs_values(num_string))
