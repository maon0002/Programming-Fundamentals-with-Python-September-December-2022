import re

number_of_messages = int(input())
attacked_planets = []
destroyed_planets = []

for messages in range(number_of_messages):
    command = input()
    pattern = r'[star]'
    star_match = re.findall(pattern, command, re.I)
    encryption_key = len(star_match)
    encoded_message = ""
    for i in range(len(command)):
        current_char = command[i]
        new_char = chr(ord(current_char) - encryption_key)
        encoded_message += new_char
    # print(encoded_message)
    pattern_after_decoding = r'@([A-Za-z]+)[^@\-!:>]*:[^@\-!:>\d]*(\d+)[^@\-!:>\d]*![^@\-!:>]*(A|D)[^@\-!:>]*![^@\-!:>]*->[^@\-!:>\d]*(\d+)[^@\-!:>]*'
    matches = re.search(pattern_after_decoding, encoded_message)
    if matches:
        planet_name, planet_population, attack_type, soldier_count = re.search(pattern_after_decoding,
                                                                               encoded_message).groups()

        if attack_type == "A":
            attacked_planets.append(planet_name)
        else:
            destroyed_planets.append(planet_name)

attacked_planets = sorted(attacked_planets, key=lambda x: x)
destroyed_planets = sorted(destroyed_planets, key=lambda x: x)
print(f"Attacked planets: {len(attacked_planets)}")
for planet in attacked_planets:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in destroyed_planets:
    print(f"-> {planet}")

# 5
# STCDoghudd4=63333$D$0A53333
# EHfsytsnhf?8555&I&2C9555SR
# tt(''DGsvywgerx>6444444444%H%1B9444
# GQhrr|A977777(H(TTTT
# EHfsytsnhf?8555&I&2C9555SR
