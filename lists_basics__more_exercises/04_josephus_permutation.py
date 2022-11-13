people = input().split()
kill_position = int(input())
killed_people_list = []
step_counter = 0
step_index = 0
while len(people) > 0:
    step_counter += 1
    if step_counter % kill_position == 0:
        killed_people_list.append(int(people.pop(step_index)))
    else:
        step_index += 1

    if step_index >= len(people):
        step_index = 0
killed_people_list = str(killed_people_list).replace(' ', "")
print(killed_people_list)
