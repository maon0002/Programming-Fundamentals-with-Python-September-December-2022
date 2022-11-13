position_list = []

for position in range(3):
    command = input()
    position_list.append(command)

position_list[0], position_list[2] = position_list[2], position_list[0]

print(position_list)
