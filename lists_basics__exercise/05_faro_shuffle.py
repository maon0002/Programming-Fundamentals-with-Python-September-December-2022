cards = input().split()
number_of_shuffles = int(input())
split_number = len(cards) // 2
left_deck = cards[:split_number]
right_deck = cards[-split_number:]

shuffle_counter = 0

while shuffle_counter < number_of_shuffles:
    current_shuffle = []

    for i in range(len(left_deck)):
        current_shuffle.append(left_deck[i])
        current_shuffle.append(right_deck[i])

    left_deck = current_shuffle[:split_number]
    right_deck = current_shuffle[-split_number:]
    shuffle_counter += 1

print(current_shuffle)
