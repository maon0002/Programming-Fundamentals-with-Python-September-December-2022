def chairs_calc(rooms, chairs, people):
    needed_chairs_in_room = abs(chairs - people)
    if free_chairs < incomming_people:
        print(f"{needed_chairs_in_room} more chairs needed in room {rooms}")


diff_chairs = 0
rooms_number = int(input())
for space in range(1, rooms_number + 1):
    chairs_and_people = input().split()

    free_chairs = (chairs_and_people[0]).count("X")
    incomming_people = int(chairs_and_people[-1])
    chairs_calc(space, free_chairs, incomming_people)
    diff_chairs += (free_chairs - incomming_people)

if diff_chairs >= 0:
    print(f"Game On, {diff_chairs} free chairs left")
