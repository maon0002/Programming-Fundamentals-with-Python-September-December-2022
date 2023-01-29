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
