# Problem 1 - World Tour
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#0.
#
# You are a world traveler, and your next goal is to make a world tour. To do that, you have to plan out everything first. To start with, you would like to plan out all of your stops where you will have a break.
# On the first line, you will be given a string containing all of your stops. Until you receive the command "Travel", you will be given some commands to manipulate that initial string. The commands can be:
#     • "Add Stop:{index}:{string}":
#         ◦ Insert the given string at that index only if the index is valid
#     • "Remove Stop:{start_index}:{end_index}":
#         ◦ Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
#     • "Switch:{old_string}:{new_string}":
#         ◦ If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string if it is valid!
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
# Input / Constraints
#     • JavaScript: you will receive a list of strings
#     • An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.
# Output
#     • Print the proper output messages in the proper cases as described in the problem description


def add_stop(index, string, upd_destinations):
    if 0 <= index <= len(upd_destinations):
        upd_destinations = upd_destinations[0:index] + string + upd_destinations[index:]
        print(upd_destinations)
    return upd_destinations


def remove_stop(start_index, end_index, upd_destinations):
    if (0 <= start_index <= len(upd_destinations)) and (0 <= end_index <= len(upd_destinations) - 1):
        first_part = upd_destinations[:start_index]
        second_part = upd_destinations[end_index + 1:]
        upd_destinations = first_part + second_part
    print(upd_destinations)
    return upd_destinations


def switch(old_string, new_string, upd_destinations):
    if old_string in upd_destinations:
        upd_destinations = upd_destinations.replace(old_string, new_string,)
    print(upd_destinations)
    return upd_destinations


def main(init_destinations):
    upd_destinations = init_destinations
    while True:
        command_line = input()
        if command_line == "Travel":
            break

        command, value_one, value_two = command_line.split(":")
        if command == "Add Stop":
            upd_destinations = add_stop(int(value_one), value_two, upd_destinations)
        elif command == "Remove Stop":
            upd_destinations = remove_stop(int(value_one), int(value_two), upd_destinations)
        elif command == "Switch":
            upd_destinations = switch(value_one, value_two, upd_destinations)
    print(f"Ready for world tour! Planned stops: {upd_destinations}")


stops = input()
main(stops)

