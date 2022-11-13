phone_name_input = input().split("-")
phonebook_dictionary = {}
while len(phone_name_input) == 2:
    name, phone_number = phone_name_input
    phonebook_dictionary[name] = phone_number

    phone_name_input = input().split("-")

for names in range(int(phone_name_input[0])):
    searching_for = input()
    if searching_for in phonebook_dictionary.keys():
        print(f"{searching_for} -> {phonebook_dictionary[searching_for]}")
    else:
        print(f"Contact {searching_for} does not exist.")
