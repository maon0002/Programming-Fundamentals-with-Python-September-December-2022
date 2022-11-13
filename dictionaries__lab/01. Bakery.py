input_string = input().split()
bakery_dictionary = {}
for index in range(0, len(input_string), 2):
    food = input_string[index]
    qty = input_string[index + 1]
    bakery_dictionary[food] = int(qty)

print(bakery_dictionary)
