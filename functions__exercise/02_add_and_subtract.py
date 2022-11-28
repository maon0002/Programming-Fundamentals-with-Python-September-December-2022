#     2. Add and Subtract
# You will receive three integer numbers.
# Write functions named:
#     • sum_numbers() that returns the sum of the first two integers
#     • subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters. Print the result of the subtract() function on the console.


def sum_numbers(num1, num2, num3):
    result = num1 + num2
    subtract(result, num3)


def subtract(sum_result, num3):
    result = sum_result - num3
    print(result)


first_number, second_number, third_number = int(input()), int(input()), int(input())
sum_numbers(first_number, second_number, third_number)
