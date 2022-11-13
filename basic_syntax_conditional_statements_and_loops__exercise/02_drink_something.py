age = int(input())
beverage = ''

if age <= 14:
    beverage = 'toddy'
    print(f"drink {beverage}")
elif age <= 18:
    beverage = 'coke'
    print(f"drink {beverage}")
elif age <= 21:
    beverage = 'beer'
    print(f"drink {beverage}")
else:
    beverage = 'whisky'
    print(f"drink {beverage}")
