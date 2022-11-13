contest_dict = {}

while True:
    command = input()
    if command == "end of contests":
        break

    contest, password = command.split(":")
    contest_dict[contest] = password

person_records = {}

while True:
    correct_pass = True
    correct_contest = True
    command2 = input()
    if command2 == "end of submissions":
        break

    contest, password, username, points = command2.split("=>")
    if contest not in contest_dict.keys():
        correct_contest = False
    correct_pass = ({key: value for (key, value) in contest_dict.items() if (contest, password) == (key, value)} != {})

    if correct_contest and correct_pass:

        if username not in person_records.keys():
            person_records[username] = [[], []]
        if contest in person_records[username][0]:
            index = person_records[username][0].index(contest)
            if person_records[username][1][index] < int(points):
                person_records[username][1][index] = int(points)
        else:
            person_records[username][0].append(contest)
            person_records[username][1].append(int(points))

final_dict = {}

for key, value in person_records.items():
    user = key
    total = sum(value[1])
    final_dict[user] = total

best_candidate = [key for key, value in final_dict.items() if value == max(final_dict.values())]
best_score = [value for key, value in final_dict.items() if value == max(final_dict.values())]
print(f"Best candidate is {best_candidate[0]} with total {best_score[0]} points.")
print(f"Ranking:")

for name, value in sorted(person_records.items()):
    user_name = name
    print(user_name)
    index = 0
    for val in sorted(reversed(person_records[user_name][1]), reverse=True):
        i = person_records[user_name][1].index(val)
        course = person_records[user_name][0][i]
        print(f"#  {course} -> {val}")
