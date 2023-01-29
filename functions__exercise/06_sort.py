
def sort_func(base_list):
    sorted_list = sorted(base_list)
    print(sorted_list)


input_line = list(map(int, input().split(" ")))
sort_func(input_line)
