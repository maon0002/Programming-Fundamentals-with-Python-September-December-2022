miner_dictionary = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in miner_dictionary.keys():
        miner_dictionary[resource] = 0
    miner_dictionary[resource] += quantity

for resources, quantities in miner_dictionary.items():
    print(f"{resources} -> {quantities}")
