def print_result(town_dict):
    count = len(town_dict.keys())
    if count > 0:
        print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
        for key, value in town_dict.items():
            print_town = key
            print_people = value[0]
            print_gold = value[1]
            print(f"{print_town} -> Population: {print_people} citizens, Gold: {print_gold} kg")
        return f"Ahoy, Captain! There are {count} wealthy settlements to go to:"
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
    return "Ahoy, Captain! All targets have been plundered and destroyed!"


def plunder(current_town, people, stolen_gold, town_dict):
    print(f"{current_town} plundered! {stolen_gold} gold stolen, {people} citizens killed.")
    town_dict[current_town][0] -= people
    town_dict[current_town][1] -= stolen_gold
    if not town_dict[current_town][0] or not town_dict[current_town][1]:
        del town_dict[current_town]
        print(f"{current_town} has been wiped off the map!")
        return town_dict
    return town_dict


def prosper(current_town, add_gold, town_dict):
    if add_gold < 0:
        print("Gold added cannot be a negative number!")
        return town_dict
    town_dict[current_town][1] += add_gold
    print(f"{add_gold} gold added to the city treasury. {current_town} now has {town_dict[current_town][1]} gold.")
    return town_dict


def actions(town_dict):
    while True:
        action_command = input()
        if action_command == "End":
            print_result(town_dict)
            break
        current_line = action_command.split("=>")
        current_action = current_line[0]
        current_town = current_line[1]

        if current_action == "Plunder":
            people = int(current_line[2])
            stolen_gold = int((current_line[3]))
            town_dict = plunder(current_town, people, stolen_gold, town_dict)
        elif current_action == "Prosper":
            add_gold = int((current_line[2]))
            town_dict = prosper(current_town, add_gold, town_dict)


def before_sail():
    town_dict = {}
    while True:
        command = input()
        if command == "Sail":
            actions(town_dict)
            break
        current_command = command.split("||")
        town = current_command[0]
        population = int(current_command[1])
        gold = int(current_command[2])
        if town in town_dict:
            town_dict[town][0] += population
            town_dict[town][1] += gold
        else:
            town_dict[town] = [population, gold]


before_sail()
