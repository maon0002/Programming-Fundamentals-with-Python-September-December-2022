#     10. Perfect Number
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
#     • "We have a perfect number!" - if the number is perfect.
#     • "It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.

def perfect_num(num):
    temp_num = num
    divisors = int(num / 2 + 1)
    divisors_list = []
    # while temp_num > 0:
    for nums in range(divisors, 0, -1):
        if temp_num % nums == 0:
            divisors_list.append(nums)
            continue

    if sum(divisors_list) == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num_input = int(input())
perfect_num(num_input)
