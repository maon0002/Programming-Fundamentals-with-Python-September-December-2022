def calculator(operator, num_one, num_two):
    if operator == "multiply":
        return num_one * num_two
    elif operator == "divide":
        return num_one // num_two
    elif operator == "add":
        return num_one + num_two
    elif operator == "subtract":
        return num_one - num_two


operator_input = input()
first_num = int(input())
second_num = int(input())
print(calculator(operator_input, first_num, second_num))
