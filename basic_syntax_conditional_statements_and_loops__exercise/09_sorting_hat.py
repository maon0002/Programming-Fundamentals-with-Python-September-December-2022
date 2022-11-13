command = input()
is_voldemort_name_mentioned = False

while command != "Welcome!":
    name = command
    if command == "Voldemort":
        is_voldemort_name_mentioned = True
        print("You must not speak of that name!")
        break
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")

    command = input()

if not is_voldemort_name_mentioned:
    print("Welcome to Hogwarts.")
