lines_number = int(input())

for x in range(lines_number):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f'{current_number} is odd!')
        break
else:
    print(f'All numbers are even.')
