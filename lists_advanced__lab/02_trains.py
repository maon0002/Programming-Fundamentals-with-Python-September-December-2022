train_length = int(input())
wagons = [0] * train_length

while True:
    command = input()
    split_command = command.split()
    current_command = split_command[0]

    if current_command == "End":
        break

    people = int(split_command[-1])
    index = int(split_command[1])

    if current_command == "add":
        wagons[-1] += people

    elif current_command == "insert":
        wagons[index] += people

    elif current_command == "leave":
        wagons[index] -= people

print(wagons)
