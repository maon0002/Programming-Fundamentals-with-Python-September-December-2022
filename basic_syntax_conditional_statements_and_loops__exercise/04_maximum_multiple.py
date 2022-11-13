positive_divisor = int(input())
positive_boundary = int(input())
max_multiplayer = 0

for i in range(1, positive_boundary + 1):
    calc = i % positive_divisor
    if calc == 0:
        max_multiplayer = i

print(max_multiplayer)
