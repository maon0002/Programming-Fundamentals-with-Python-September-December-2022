#   fancy barcodes

import re

number_of_barcodes = int(input())

for _ in range(number_of_barcodes):
    barcode = input()
    pattern = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)'
    result = re.match(pattern, barcode)

    if not result:
        print('Invalid barcode')
    else:
        extract_nums = re.findall('\d', result.group())

        if not extract_nums:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(extract_nums)}")


# The pianist

def store_data_func(number):
    data = {}
    for _ in range(number):
        current_data = input().split('|')
        piece = current_data[0]
        composer = current_data[1]
        key = current_data[2]

        data[piece] = [composer, key]

    return data


def add_command_function(piece, composer, key, data):
    if piece not in data:
        data[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove_function(piece, data):
    if piece in data:
        print(f"Successfully removed {piece}!")
        del data[piece]
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key_function(piece, new_key, data):
    if piece in data:
        # Our dictionary for example ---> {'Fur Elise': ['Beethoven', 'A Minor']}
        # At the index 0 in list is composer, at the index 1 is a specific key
        data[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def print_function(data):
    result = ''
    for piece in data:
        composer = data[piece][0]
        key = data[piece][1]
        result += f"{piece} -> Composer: {composer}, Key: {key}\n"

    return result


# Our core function that navigates our entire program. Each time in it
# we will accept one element as a parameter -- > number of pieces
def the_pianist_func(number):
    # store_data_func returns a dictionary containing as key the name of
    # pieces and as value containing a list of two elements. At index 0 in
    # the list is the name of composer, and at the index 1 in the list is
    # specific key
    data = store_data_func(number)

    while True:
        command = input().split('|')

        if command[0] == 'Stop':
            print(print_function(data))
            break

        current_command = command[0]
        piece = command[1]

        if current_command == 'Add':
            composer = command[2]
            key = command[3]
            add_command_function(piece, composer, key, data)

        elif current_command == 'Remove':
            remove_function(piece, data)

        elif current_command == 'ChangeKey':
            new_key = command[2]
            change_key_function(piece, new_key, data)


number_of_pieces = int(input())
the_pianist_func(number_of_pieces)

# destination mapper
import re

data = input()
pattern = r'(=|\/)[A-Z][A-Za-z]{2,}\1'
result = re.finditer(pattern, data)

points = 0
all_destinations = []

for destination in result:
    current_destination = re.split('\/|=', destination.group())[1]
    points += len(current_destination)
    all_destinations.append(current_destination)

print(f"Destinations: {', '.join(all_destinations)}")
print(f"Travel Points: {points}")

# secret chat

data = input()

while True:

    command = input().split(':|:')
    current_command = command[0]

    if current_command == 'Reveal':
        print(f"You have a new text message: {data}")
        break

    elif current_command == 'InsertSpace':
        index = int(command[1])
        data = data[:index] + ' ' + data[index:]
        print(data)

    elif current_command == 'Reverse':
        substring = command[1]
        if substring in data:
            data = data.replace(substring, '', 1)
            data = data + substring[::-1]
            print(data)
        else:
            print('error')

    elif current_command == 'ChangeAll':
        substring, replacement = command[1], command[2]
        data = data.replace(substring, replacement)
        print(data)

# ad astra

import re

data = input()
pattern = r'(\#|\|)([a-z A-Z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
result = re.findall(pattern, data)
print_result = ''
calories = 0

for elements in result:
    print_result += f"Item: {elements[1]}, Best before: {elements[2]}, Nutrition: {elements[3]}\n"
    calories += int(elements[-1])

number_of_days = int(calories / 2000)
print(f"You have food to last you for: {number_of_days} days!")
print(print_result)


# world tour
def world_tour(destinations):
    while True:
        command = input().split(':')
        current_command = command[0]

        if current_command == 'Travel':
            print(f'Ready for world tour! Planned stops: {destinations}')
            break

        elif current_command == 'Add Stop':
            index, string = int(command[1]), command[2]

            if 0 <= index < len(destinations):
                destinations = destinations[:index] + string + destinations[index:]

        elif current_command == 'Remove Stop':
            start_index, end_index = int(command[1]), int(command[2])

            if 0 <= start_index <= end_index < len(destinations):
                destinations = destinations[:start_index] + destinations[end_index + 1:]

        elif current_command == 'Switch':
            old_string, new_string = command[1], command[2]
            destinations = destinations.replace(old_string, new_string)

        print(destinations)


data = input()
world_tour(data)


# heroes of code and logic
def create_heroes(heroes_dict, number):
    for _ in range(number):
        data = input().split(' ')
        hero_name, hit_points, mana_points = data[0], int(data[1]), int(data[2])
        heroes_dict[hero_name] = [hit_points, mana_points]


def playing_game(heroes_dict):
    while True:
        command = input().split(' - ')

        if command[0] == 'End':
            break

        current_command = command[0]

        if current_command == 'CastSpell':
            hero_name, mp_needed, spell_name = command[1], int(command[2]), command[3]
            available_mp = heroes_dict[hero_name][1]

            if available_mp >= mp_needed:
                heroes_dict[hero_name][1] -= mp_needed
                current_mp = heroes_dict[hero_name][1]
                print(f"{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif current_command == 'TakeDamage':
            hero_name, damage, attacker = command[1], int(command[2]), command[3]
            available_hp = heroes_dict[hero_name][0]

            if available_hp - damage > 0:
                heroes_dict[hero_name][0] -= damage
                current_hp = heroes_dict[hero_name][0]
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
            else:
                del heroes_dict[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif current_command == 'Recharge':
            hero_name, amount = command[1], int(command[2])
            available_mp = heroes_dict[hero_name][1]

            if available_mp + amount > 200:
                amount = 200 - available_mp
                heroes_dict[hero_name][1] += amount
            else:
                heroes_dict[hero_name][1] += amount

            print(f"{hero_name} recharged for {amount} MP!")

        elif current_command == 'Heal':
            hero_name, amount = command[1], int(command[2])
            available_mp = heroes_dict[hero_name][0]

            if available_mp + amount > 100:
                amount = 100 - available_mp
                heroes_dict[hero_name][0] += amount
            else:
                heroes_dict[hero_name][0] += amount

            print(f"{hero_name} healed for {amount} HP!")


def print_function(heroes_dict):
    print_result = ''

    for hero in heroes_dict:
        print_result += f'{hero}\n  HP: {heroes_dict[hero][0]}\n  MP: {heroes_dict[hero][1]}\n'

    return print_result


def heroes_of_code(number):
    # In heroes_dict we have key - hero name and as value we have
    # a list with two elements: HP - index 0, MP - index 1
    heroes_dict = {}

    # This function will create our heroes by adding different specifics for them
    # like HP and MP. HP stands for hit po2ints and MP for mana points
    create_heroes(heroes_dict, number_of_heroes)

    # This is the main function in which the game will develop
    # according to certain conditions
    playing_game(heroes_dict)

    # print_function - Print all members of your party who are still alive
    # and their HP and MP
    print(print_function(heroes_dict))


number_of_heroes = int(input())
heroes_of_code(number_of_heroes)

# mirror words
import re

data = input()
pattern = r'(#|@)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1'
result = re.findall(pattern, data)
mirror_words = []
the_count_of_words = 0

for pair in result:
    if pair[1] == pair[3][::-1]:
        mirror_words.append(f'{pair[1]} <=> {pair[3]}')

    the_count_of_words += 1

if the_count_of_words > 0:
    print(f'{the_count_of_words} word pairs found!')

    if not mirror_words:
        print('No mirror words!')
    else:
        print('The mirror words are:')
        print(', '.join(mirror_words))

else:
    print('No word pairs found!')
    print('No mirror words!')


# decorator example
def decorator_func(fnc):
    def inner(list_of_names):
        return {val[0]: [val[1], val[2]] for val in list_of_names}

    return inner


@decorator_func
def main_function(*args):
    return args


number_of_heroes = int(input())
data = [input().split(' ') for _ in range(number_of_heroes)]
print(main_function(data))