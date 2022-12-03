#     1. Ranking
# Here comes the final and the most interesting part – the Final ranking of the candidate-interns. The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni. Here is your final task. You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests". Save that data because you will need it later. After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions". Here is what you need to do.
#     • Check if the contest is valid (It is considered valid if you received it in the first type of input)
#     • Check if the password is correct for the given contest
#     • If the contest and the password is valid, save the user with the contest they take part in (a user can take part in many contests) and the points the user has in the given contest. If you receive the same contest and the same user update the points only if the new ones are more than the older ones.
# In the end, you should print the info for the user with the most points (total points for all contents they participated in) in the format "Best candidate is {user} with total {total_points} points.". After that print all students ordered by their names. For each user print each contest with the points in descending order. See the examples.
# Input
#     • Strings in format "{contest}:{password for contest}" until the "end of contests" command. There will be no case with two equal contests
#     • Strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.
#     • There will be no case with 2 or more users with same total points!
# Output
#     • On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
#     • Then print all students ordered as mentioned above in format:
# "{user_name1}
# #  {contest1} -> {points}
# #  {contest2} -> {points}
# …
# #  {contestN} -> {points}"
# Constraints
#     • The strings may contain any ASCII character except from (:, =, >).
#     • The numbers will be in range [0 - 10000].



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
