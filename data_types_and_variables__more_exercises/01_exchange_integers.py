first_number = int(input())
second_number = int(input())
for x in range(2):
    if x == 0:
        print("Before:")
        print(f"a = {first_number}")
        print(f"b = {second_number}")
    else:
        print("After:")
        print(f"a = {second_number}")
        print(f"b = {first_number}")
