input_list = input().split()
digit_list = [int(i) for i in input_list]
descending_sort = digit_list.copy()
descending_sort.sort(reverse=True)
numbers_to_remove = int(input())

# list_of_the_smallest = descending_sort[-numbers_to_remove:]
list_of_the_biggest = descending_sort[:-numbers_to_remove]
result = []

for digit in digit_list:
    if digit in list_of_the_biggest:
        result.append(str(digit))

print(", ".join(result))
