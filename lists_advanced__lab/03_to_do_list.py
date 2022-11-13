result_list = []
initial_priority = 10
while True:
    command = input()

    if command == "End":
        break

    split_command = command.split("-")

    current_priority = int(split_command[0])
    current_action = split_command[1]

    result_list.append([current_priority, current_action])

sorted_tasks = []

for actions in sorted(result_list):
    sorted_tasks.append(actions[1])

print(sorted_tasks)
