number = int(input())

special_condition = [5, 7, 11]
current_result = 0

for i in range(1, number + 1):
    numbers = str(i)
    for j in range(len(str(i))):
        position = str(numbers[j])
        current_result += int(position)
    if current_result in special_condition:
        print(f"{i} -> True")
        current_result = 0
    else:
        print(f"{i} -> False")
        current_result = 0
