numbers_string = input().split(", ")
digits_list = [int(x) for x in numbers_string]
indexes = [i for i in range(len(digits_list)) if int(digits_list[i]) % 2 == 0]
print(indexes)
