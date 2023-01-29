
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

