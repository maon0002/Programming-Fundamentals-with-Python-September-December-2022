#     3. Star Enigma
# The war is in its peak, but you, young Padawan, can turn the tides with your programming skills. You are tasked to create a program to decrypt the messages of The Order and prevent the death of hundreds of lives.
# You will receive several messages, which are encrypted using the legendary star enigma. You should decrypt the messages, following these rules:
# To properly decrypt a message, you should count all the letters [s, t, a, r] – case insensitive and remove the count from the current ASCII value of each symbol of the encrypted message.
# After decryption:
# Each message should have a planet name, population, attack type ('A', as attack or 'D', as destruction) and soldier count.
# The planet name starts after '@' and contains only letters from the Latin alphabet.
# The planet population starts after ':' and is an Integer;
# The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
# The soldier count starts after "->" and should be an Integer.
# The order in the message should be: planet name -> planet population -> attack type -> soldier count. Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
# Input / Constraints
#     • The first line holds n – the number of messages– integer in range [1…100];
#     • On the next n lines, you will be receiving encrypted messages.
# Output
# After decrypting all messages, you should print the decrypted information in the following format:
# First print the attacked planets, then the destroyed planets.
# "Attacked planets: {attackedPlanetsCount}"
# "-> {planetName}"
# "Destroyed planets: {destroyedPlanetsCount}"
# "-> {planetName}"
# The planets should be ordered by name alphabetically.

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
