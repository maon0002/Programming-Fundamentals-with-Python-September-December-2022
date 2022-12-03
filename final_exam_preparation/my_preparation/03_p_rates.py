# Problem 3 - P!rates
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#2.
#
# Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate captain by the name of Jack Daniels. Together with your comrades Jim (Beam) and Johnny (Walker), you have been roaming the seas, looking for gold and treasure… and the occasional killing, of course. Go ahead, target some wealthy settlements and show them the pirate's way!
# Until the "Sail" command is given, you will be receiving:
#     • You and your crew have targeted cities, with their population and gold, separated by "||".
#     • If you receive a city that has already been received, you have to increase the population and gold with the given values.
# After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given.
# Events will be in the following format:
#     • "Plunder=>{town}=>{people}=>{gold}"
#         ◦ You have successfully attacked and plundered the town, killing the given number of people and stealing the respective amount of gold.
#         ◦ For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
#         ◦ If any of those two values (population or gold) reaches zero, the town is disbanded.
#             ▪ You need to remove it from your collection of targeted cities and print the following message: "{town} has been wiped off the map!"
#         ◦ There will be no case of receiving more people or gold than there is in the city.
#     • "Prosper=>{town}=>{gold}"
#         ◦ There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
#         ◦ The gold amount can be a negative number, so be careful. If a negative amount of gold is given, print: "Gold added cannot be a negative number!" and ignore the command.
#         ◦ If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the following message:
# "{gold added} gold added to the city treasury. {town} now has {total gold} gold."
# Input
#     • On the first lines, until the "Sail" command, you will be receiving strings representing the cities with their gold and population, separated by "||"
#     • On the following lines, until the "End" command, you will be receiving strings representing the actions described above, separated by "=>"
# Output
#     • After receiving the "End" command, if there are any existing settlements on your list of targets, you need to print all of them, in the following format:
# "Ahoy, Captain! There are {count} wealthy settlements to go to:
# {town1} -> Population: {people} citizens, Gold: {gold} kg
# {town2} -> Population: {people} citizens, Gold: {gold} kg
#    …
# {town…n} -> Population: {people} citizens, Gold: {gold} kg"
#     • If there are no settlements left to plunder, print:
# "Ahoy, Captain! All targets have been plundered and destroyed!"
# Constraints
#     • The initial population and gold of the settlements will be valid 32-bit integers, never negative, or exceed the respective limits.
#     • The town names in the events will always be valid towns that should be on your list.
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
