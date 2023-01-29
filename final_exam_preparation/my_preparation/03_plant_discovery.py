def rate_func(current_value, working_plants_dictionary):
    current_plant, current_rating = current_value.split(" - ")
    working_plants_dictionary[current_plant][1].append(int(current_rating))
    return working_plants_dictionary


def update_func(current_value, working_plants_dictionary):
    current_plant, new_rarity = current_value.split(" - ")
    working_plants_dictionary[current_plant][0] = int(new_rarity)
    return working_plants_dictionary


def reset_func(current_value, working_plants_dictionary):
    current_plant = current_value
    working_plants_dictionary[current_plant][1] = []
    return working_plants_dictionary


def initial_plant_storage(num_of_plants):
    initial_plant_dictionary = {}
    for num in range(num_of_plants):
        plant, rarity = input().split("<->")
        initial_plant_dictionary[plant] = [int(rarity), []]
        num_of_plants -= 1
    actions(initial_plant_dictionary)
    return initial_plant_dictionary


def print_and_rate(dictionary):
    print("Plants for the exhibition:")
    for item in dictionary.items():
        plant_name = item[0]
        plant_rarity = item[1][0]
        plant_total_ranks = sum(item[1][1])
        plant_ranks_length = len(item[1][1])
        if plant_ranks_length:
            average_rating = plant_total_ranks / plant_ranks_length
            print(f"- {plant_name}; Rarity: {plant_rarity}; Rating: {average_rating:.2f}")
        else:
            print(f"- {plant_name}; Rarity: {plant_rarity}; Rating: 0.00")
    return dictionary


def plant_validation(working_plants_dictionary, current_value):
    current_plant = current_value.split(" - ")
    if current_plant[0] in working_plants_dictionary.keys():
        return True
    return False


def actions(initial_plants_dict):
    working_plants_dictionary = initial_plants_dict.copy()

    while True:
        command = input()
        if command == "Exhibition":
            print_and_rate(working_plants_dictionary)
            break

        current_action, current_value = command.split(": ")

        if not plant_validation(working_plants_dictionary, current_value):
            print("error")
            continue

        if current_action == "Rate":
            working_plants_dictionary = rate_func(current_value, working_plants_dictionary)
        elif current_action == "Update":
            working_plants_dictionary = update_func(current_value, working_plants_dictionary)
        elif current_action == "Reset":
            working_plants_dictionary = reset_func(current_value, working_plants_dictionary)

    return working_plants_dictionary


number_of_plants = int(input())
initial_plant_storage(number_of_plants)
