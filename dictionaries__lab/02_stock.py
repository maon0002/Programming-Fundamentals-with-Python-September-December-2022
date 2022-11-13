in_stock_products = input().split(' ')
in_stock_products_dict = {}

for index in range(0, len(in_stock_products), 2):
    food = in_stock_products[index]
    qty = in_stock_products[index + 1]
    in_stock_products_dict[food] = qty

searching_for = input().split()
for searched_food in searching_for:

    if searched_food in in_stock_products_dict.keys():
        print(f"We have {in_stock_products_dict[searched_food]} of {searched_food} left")
    else:
        print(f"Sorry, we don't have {searched_food}")
