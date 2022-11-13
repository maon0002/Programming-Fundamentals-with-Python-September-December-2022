number_of_commands = int(input())
reg_dict = {}
final_dict = {}
for times in range(number_of_commands):
    command_line = input().split()
    command = command_line[0]
    name = command_line[1]

    if command == "register":
        plate = command_line[2]
        if name not in reg_dict.keys():
            reg_dict[name] = plate
            final_dict[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif command == "unregister":
        if name not in reg_dict.keys():
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
        if name in final_dict.keys():
            del final_dict[name]

for username, license_plate_number in final_dict.items():
    print(f"{username} => {license_plate_number}")
