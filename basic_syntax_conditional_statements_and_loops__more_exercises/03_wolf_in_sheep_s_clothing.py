text = input()
queue = list(text.split(", "))

nearest_animal = len(queue) - 1
is_wolf_next = False
counter_animals = 0

for position in range(len(queue), 0, -1):
    i = position - 1
    animal = queue[i]

    if animal == 'wolf' and i == nearest_animal:
        is_wolf_next = True

        break
    elif animal == 'wolf':
        break
    counter_animals += 1

if is_wolf_next:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {counter_animals}! You are about to be eaten by a wolf!")
