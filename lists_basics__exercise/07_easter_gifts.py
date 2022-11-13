gifts_list_input = input().split()
command = input()
gifts_list = gifts_list_input.copy()

while command != "No Money":
    command_list = command.split()
    index_gift = ""

    if "OutOfStock" in command_list:
        for gift in gifts_list:
            if gift in command_list:
                index_gift = gifts_list.index(gift)
                gifts_list[index_gift] = "None"
    elif "Required" in command_list:
        command_index = int(command_list[-1])
        replace_gift_with = command_list[1]
        if command_index < len(gifts_list):
            gifts_list[command_index] = replace_gift_with
    elif "JustInCase" in command_list:
        replace_gift_with = command_list[1]
        gifts_list[-1] = replace_gift_with
    command = input()

for nones in gifts_list:
    if nones == "None":
        gifts_list.remove(nones)

print(" ".join(gifts_list))
