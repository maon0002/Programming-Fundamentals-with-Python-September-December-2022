#     2. Judge
# You know the judge system, right?! Your job is to create a program similar to the Judge system.
# You will receive several input lines in one of the following formats:
# "{username} -> {contest} -> {points}"
# The "contest" and "username" are strings, the given "points" will be an integer number. You need to keep track of every contest and points of each user:
#     • If the user has already participated in the contest, update their points only if the new ones are more than the older ones.
#     • Otherwise, just save the data - contest, username, and points.
# Also, you need to keep individual statistics for each user - his/her final total points for all contests.
# You should end your program when you receive the command "no more time". At that point, you should print each contest in order of input, for each contest print the participants ordered by points in descending order, then ordered by name in ascending order. After that, you should print individual statistics for every participant ordered by total points in descending order, and then by alphabetical order.
# Input / Constraints
#     • The input comes in the form of commands in one of the formats specified above.
#     • Username and contest name always will be one word.
#     • Points will be an integer in the range [0, 1000].
#     • There will be no invalid input lines.
#     • If all sorting criteria fail, the order should be by order of input.
#     • The input ends when you receive the command "no more time".
# Output
#     • The output format for the contests is:
# "{constest_name}: {number_participants} participants
# 1. {username1} <::> {points}
# 2. {username2} <::> {points}
# …
# {N}. {usernameN} <::> {points}"
#     • After you print all contests, print the individual statistics for every participant.
#     • The output format is:
# "Individual standings:
#     1. {username1} -> {total_points}
#     2. {username} -> {total_points}
# …
# {N}. {username} -> {total_points}"

def stats(sorted_stats):
    print(sorted_stats)


# {'Peter': ['OOP', 350], 'George': ['OOP', 300], 'Simo': ['Advanced', 600], 'Prakash': ['OOP', 300, 'Advanced', 250], 'Ani': ['JSCore', 400]}
# [('Simo', 600), ('Prakash', 550), ('Ani', 400), ('Peter', 350), ('George', 300)]
def print_result(contest_dict, user_dict, sorted_stats):
    print(user_dict)
    print(contest_dict)

    # for key, value in contest_dict:
    #     current_contest = key

    stats(sorted_stats)


def individual_statistics():
    pass


def dict_manager(username, contest, points, contest_dict, user_dict, sorted_stats):
    if username not in user_dict.keys():
        user_dict[username] = [contest, points]
    if user_dict[username][0] == contest and user_dict[username][1] < points:
        user_dict[username][1] = points
    if user_dict[username][0] != contest:
        user_dict[username] += contest, points

    # if username not in contest_dict.values():
    #     contest_dict[contest] = [username, points]
    # if contest_dict[contest][0] == username and contest_dict[contest][1] < points:
    #     contest_dict[contest][1] = points
    # if contest_dict[contest][0] != username:
    #     contest_dict[contest] += username, points #[]

    if username not in contest_dict.values():
        contest_dict[contest] = username, points
    else:
        if contest_dict[contest][1] < points:
            contest_dict[contest][1] = points
    print(contest_dict.items())

    if contest_dict[contest][0] != username:
        contest_dict[contest] += username, points  # []

    counter = 0
    individual_stats = {}
    for key, value in user_dict.items():
        name = key
        total = 0
        counter += 1
        for current_value in value:
            if type(current_value) == int:
                total += current_value
        individual_stats[name] = total
    sorted_stats = sorted(individual_stats.items(), key=lambda x: x[1], reverse=True)
    return contest_dict, user_dict, sorted_stats


def judge(contest_dict, user_dict):
    sorted_stats = {}
    while True:
        command = input()
        if command == "no more time":
            print_result(contest_dict, user_dict, sorted_stats)
            break
        # current_line = command.split(" -> ")
        username, contest, points = command.split(" -> ")
        points = int(points)
        contest_dict, user_dict, sorted_stats = dict_manager(username, contest, points, contest_dict, user_dict,
                                                             sorted_stats)


user_dict = {}
contest_dict = {}
judge(contest_dict, user_dict)
