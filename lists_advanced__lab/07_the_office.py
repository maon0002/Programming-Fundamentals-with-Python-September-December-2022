def ratio(nums):
    factored_list = [x * improvement_factor for x in nums]
    limit = sum(factored_list) / len(nums)
    filtered_list = list(filter(lambda x: x >= limit, factored_list))
    if len(filtered_list) >= len(factored_list) / 2:
        return f"Score: {len(filtered_list)}/{len(factored_list)}. Employees are happy!"
    else:
        return f"Score: {len(filtered_list)}/{len(factored_list)}. Employees are not happy!"


happiness_string = input().split()
improvement_factor = int(input())

happiness_int_list = list(map(int, happiness_string))
print(ratio(happiness_int_list))
