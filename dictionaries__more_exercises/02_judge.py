
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
