# Problem 3 - Heroes of Code and Logic VII
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2303#0.
#
# You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic. You want to play it all day long! So cancel all other arrangements and create your party!
# On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for your party. On the next n lines, the heroes themselves will follow with their hit points and mana points separated by a single space in the following format:
# "{hero name} {HP} {MP}"
#     • HP stands for hit points and MP for mana points
#     • a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game. You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given.
# There are several actions that the heroes can perform:
# "CastSpell – {hero name} – {MP needed} – {spell name}"
#     • If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
#         ◦ "{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
#     • If the hero is unable to cast the spell print:
#         ◦ "{hero name} does not have enough MP to cast {spell name}!"
# "TakeDamage – {hero name} – {damage} – {attacker}"
#     • Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
#         ◦ "{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
#     • If the hero has died, remove him from your party and print:
#         ◦ "{hero name} has been killed by {attacker}!"
# "Recharge – {hero name} – {amount}"
#     • The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200. (the MP can't go over the maximum value).
#     •  Print the following message:
#         ◦ "{hero name} recharged for {amount recovered} MP!"
# "Heal – {hero name} – {amount}"
#     • The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100), HP is increased to 100 (the HP can't go over the maximum value).
#     •  Print the following message:
#         ◦ "{hero name} healed for {amount recovered} HP!"
# Input
#     • On the first line of the standard input, you will receive an integer n
#     • On the following n lines, the heroes themselves will follow with their hit points and mana points separated by a space in the following format
#     • You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given
# Output
#     • Print all members of your party who are still alive, in the following format (their HP/MP need to be indented 2 spaces):
# "{hero name}
#   HP: {current HP}
#   MP: {current MP}"
# Constraints
#     • The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative or exceed the respective limits.
#     • The HP/MP amounts in the commands will never be negative.
#     • The hero names in the commands will always be valid members of your party. No need to check that explicitly.


def print_result(heroes_dict):
    for heroes in heroes_dict.items():
        hero_name = heroes[0]
        current_hp = heroes[1][0]
        current_mp = heroes[1][1]
        print(f"{hero_name}")
        print(f"  HP: {current_hp}")
        print(f"  MP: {current_mp}")


def cast_spell(hero_name, mp_needed, spell_name, heroes_dict):
    if heroes_dict[hero_name][1] >= mp_needed:
        heroes_dict[hero_name][1] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!")
        return heroes_dict
    print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    return heroes_dict


def take_damage(hero_name, damage, attacker, heroes_dict):
    heroes_dict[hero_name][0] -= damage
    if heroes_dict[hero_name][0] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name][0]} HP left!")
        return heroes_dict
    del heroes_dict[hero_name]
    print(f"{hero_name} has been killed by {attacker}!")
    return heroes_dict


def recharge(hero_name, amount, heroes_dict):
    max_mp = 200
    diff = max_mp - heroes_dict[hero_name][1]
    heroes_dict[hero_name][1] += amount
    if heroes_dict[hero_name][1] > max_mp:
        print(f"{hero_name} recharged for {diff} MP!")
        heroes_dict[hero_name][1] = max_mp
        return heroes_dict
    print(f"{hero_name} recharged for {amount} MP!")
    return heroes_dict


def heal(hero_name, amount, heroes_dict):
    max_hp = 100
    diff = max_hp - heroes_dict[hero_name][0]
    heroes_dict[hero_name][0] += amount
    if heroes_dict[hero_name][0] > max_hp:
        print(f"{hero_name} healed for {diff} HP!")
        heroes_dict[hero_name][0] = max_hp
        return heroes_dict
    print(f"{hero_name} healed for {amount} HP!")
    return heroes_dict


def commands(heroes_dict):
    while True:
        command = input()
        if command == "End":
            print_result(heroes_dict)
            break

        current_command = command.split(" - ")
        action = current_command[0]
        hero_name = current_command[1]
        if action == "CastSpell":
            mp_needed = int(current_command[2])
            spell_name = current_command[3]
            heroes_dict = cast_spell(hero_name, mp_needed, spell_name, heroes_dict)
        elif action == "TakeDamage":
            damage = int(current_command[2])
            attacker = current_command[3]
            heroes_dict = take_damage(hero_name, damage, attacker, heroes_dict)
        elif action == "Recharge":
            recharge_amount = int(current_command[2])
            heroes_dict = recharge(hero_name, recharge_amount, heroes_dict)
        elif action == "Heal":
            heal_amount = int(current_command[2])
            heroes_dict = heal(hero_name, heal_amount, heroes_dict)


def hit_and_mana_points(num):
    heroes_dict = {}
    for current_command in range(num):
        hero_name, hp, mp = input().split(" ")
        heroes_dict[hero_name] = [int(hp), int(mp)]
    commands(heroes_dict)


number_of_heroes = int(input())
hit_and_mana_points(number_of_heroes)
