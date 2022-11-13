input_string = input().split(":")
dictionary = {}
while len(input_string) > 1:
    name, sys_id, course = input_string
    if course not in dictionary.keys():
        dictionary[course] = []
    dictionary[course].append(f"{name} - {sys_id}")

    input_string = input().split(":")

searched_course = input_string[0].replace("_", " ")
for student in dictionary[searched_course]:
    print(student)
