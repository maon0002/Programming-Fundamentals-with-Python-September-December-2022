course_dict = {}
while True:
    command = input()
    if command == "end":
        break
    course, names = command.split(" : ")
    if course not in course_dict.keys():
        course_dict[course] = []
    course_dict[course].append(names)

for course_name in course_dict.keys():
    print(f"{course_name}: {len(course_dict[course_name])}")
    for student_name in course_dict[course_name]:
        print(f"-- {student_name}")
