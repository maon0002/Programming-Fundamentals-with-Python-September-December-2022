def sum_numbers(num1, num2, num3):
    result = num1 + num2
    subtract(result, num3)


def subtract(sum_result, num3):
    result = sum_result - num3
    print(result)


first_number, second_number, third_number = int(input()), int(input()), int(input())
sum_numbers(first_number, second_number, third_number)
