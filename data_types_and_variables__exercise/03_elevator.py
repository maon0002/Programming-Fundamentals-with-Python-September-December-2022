people = int(input())
elevator_capacity = int(input())

full_course = people // elevator_capacity
partial_course = people % elevator_capacity

if people <= elevator_capacity:
    print("1")
elif partial_course != 0:
    print(full_course + 1)
else:
    print(full_course)

#
# people = int(input())
# elevator_capacity = int(input())
# # people = 100
# # elevator_capacity = 3
#
# # capacity_formula = int(people / elevator_capacity)
# full_course = people // elevator_capacity
# partial_course = people % elevator_capacity
#
# # if people <= elevator_capacity:
# #     print("All the persons fit inside the elevator.")
# #     print("Only one course is needed.")
# # elif partial_course == 0:
# #     print(f"{full_course} courses * {elevator_capacity} people")
# # else:
# #     print(f"{full_course} courses * {elevator_capacity} people \
# # + 1 course * {partial_course} persons")
#
# if people <= elevator_capacity:
#     print("1")
# elif partial_course != 0:
#     print(full_course + 1)
# else:
#     print(full_course)
