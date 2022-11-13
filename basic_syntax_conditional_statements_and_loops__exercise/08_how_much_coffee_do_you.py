command = input()
command_list = ["coding", "dog", "cat", "movie"]
coffee_counter = 0

while command != "END":
    command_check = command.lower()
    if command_check in command_list:
        if command.islower():
            coffee_counter += 1
        elif command.isupper():
            coffee_counter += 2
    command = input()

if coffee_counter <= 5:
    print(coffee_counter)
else:
    print("You need extra sleep")
