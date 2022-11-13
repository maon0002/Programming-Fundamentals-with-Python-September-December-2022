key_materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = 250
obtained = False
while not obtained:

    current_materials = input().split()
    for index in range(1, len(current_materials), 2):
        current_item = current_materials[index]
        current_item = current_item.lower()
        current_value = int(current_materials[index - 1])
        if current_item not in key_materials.keys():
            key_materials[current_item] = 0
        key_materials[current_item] += current_value

        if key_materials[current_item] >= legendary_item:
            if current_item == "shards":
                key_materials[current_item] -= legendary_item
                print(f"Shadowmourne obtained!")
                obtained = True
                break

            elif current_item == "fragments":
                key_materials[current_item] -= legendary_item
                print(f"Valanyr obtained!")
                obtained = True
                break

            elif current_item == "motes":
                key_materials[current_item] -= legendary_item
                print(f"Dragonwrath obtained!")
                obtained = True
                break

for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")
