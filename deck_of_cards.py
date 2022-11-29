import random

# permutation from import itertools
colors = ["Clubs", "Diamonds", "Hearts", "Spades"]
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = []

for value in values:
    for color in colors:
        deck.append(f"{value} - {color} ")

random.shuffle(deck)
hand = random.sample(deck, 5)

print(deck)
print(hand) # exclude hand from the deck...
