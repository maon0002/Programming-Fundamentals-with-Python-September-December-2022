inputs = int(input())
is_pure = True
not_pure_chars = [".", "_", ","]

for i in range(inputs):
    input_line = input()
    for j in range(len(input_line)):
        char = input_line[j]
        if char in not_pure_chars:
            is_pure = False

    if is_pure:
        print(f"{input_line} is pure.")
    else:
        print(f"{input_line} is not pure!")


# from re import search
#
# inputs = int(input())
#
# for i in range(inputs):
#     input_line = input()
#
#     if search("([._,])", input_line):
#         print(f"{input_line} is not pure!")
#     else:
#         print(f"{input_line} is pure.")
